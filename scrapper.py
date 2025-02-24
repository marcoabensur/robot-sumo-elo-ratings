import json
import logging
import requests
from bs4 import BeautifulSoup, Comment
from typing import List, Dict


def organize_matches(matches: List[Dict]) -> Dict[str, List[Dict]]:
    robot_losses = {}
    losers_bracket = []
    winners_bracket = []

    for match in matches:
        loser = match["loser"]["robot"]
        robot_losses[loser] = robot_losses.get(loser, 0) + 1

    is_losers = True
    for match in matches:
        loser = match["loser"]["robot"]
        if robot_losses[loser] == 3:
            is_losers = False

        if is_losers:
            losers_bracket.append(match)
        else:
            winners_bracket.append(match)

        robot_losses[loser] = robot_losses.get(loser, 0) + 1

    losers_bracket.reverse()

    return {
        "losers_bracket": losers_bracket,
        "winners_bracket": winners_bracket,
    }


def parse_match_details(
    data_src: str, winner_name: str, event_id: str, category_id: str
) -> dict:
    base_url: str = "https://events.robocore.net"
    url: str = f"{base_url}/{event_id}/brackets/{category_id}"
    match_url = f"{url}{data_src}"
    match_response = requests.get(match_url)
    match_soup = BeautifulSoup(match_response.text, "html.parser")

    team_names = [
        team.get_text(strip=True)
        for team in match_soup.find_all("div", {"class": "team_name"})
    ]
    team_robots = [
        robot.get_text(strip=True)
        for robot in match_soup.find_all("div", {"class": "team_robot"})
    ]

    if len(team_names) < 2 or len(team_robots) < 2:
        raise ValueError("Informações de equipes incompletas na partida.")
    winner_index = 0 if winner_name in team_robots[0] else 1

    return {
        "winner": {
            "team": team_names[winner_index],
            "robot": team_robots[winner_index],
        },
        "loser": {
            "team": team_names[1 - winner_index],
            "robot": team_robots[1 - winner_index],
        },
    }


def parse_brackets(soup: BeautifulSoup, event_id: str, category_id: str) -> dict:
    try:
        main_table = soup.find("table", {"id": "tblBracket"})
        match_links = main_table.find_all("a", {"data-src": True})
        match_links.pop(0)

        matches = []

        for link in match_links:
            if ">>" not in link.get_text(strip=True) and "<<" not in link.get_text(
                strip=True
            ):
                continue

            winner_name = (
                link.get_text(strip=True).replace(">>", "").replace("<<", "").strip()
            )
            data_src = link["data-src"]
            match_data = parse_match_details(
                data_src, winner_name, event_id, category_id
            )
            matches.append(match_data)

        organized_brackets = organize_matches(matches)

        return organized_brackets
    except Exception as e:
        logging.error(f"An error occurred while parsing brackets: {e}")
        raise RuntimeError("Failed to parse brackets")


def fetch_event_data(event_id: str, category_id: str) -> BeautifulSoup:
    base_url: str = "https://events.robocore.net"
    url: str = f"{base_url}/{event_id}/brackets/{category_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        if "No data found" in response.text:
            logging.warning(
                f"No data found for event {event_id} in category {category_id}"
            )
            raise FileNotFoundError(
                f"No data found for event {event_id} in category {category_id}"
            )

    except requests.exceptions.HTTPError as e:
        logging.error(
            f"Failed to fetch data for event {event_id} in category {category_id}: {e}"
        )
        raise RuntimeError(f"Failed to fetch data: {e}")

    soup = BeautifulSoup(response.text, "html.parser")
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    for unwanted_tag in ["style", "script"]:
        for tag in soup.find_all(unwanted_tag):
            tag.extract()

    return soup.body


def main(event_id: str, category_id: str):
    try:
        soup = fetch_event_data(event_id, category_id)
        brackets = parse_brackets(soup, event_id, category_id)

        final = brackets["winners_bracket"].pop()
        matches = brackets["winners_bracket"] + brackets["losers_bracket"]
        matches.append(final)

        parsed = {
            "matches": [
                [match["winner"]["team"], match["loser"]["team"]] for match in matches
            ],
            "matches-robots": [
                [match["winner"]["robot"], match["loser"]["robot"]] for match in matches
            ],
        }

        with open(event_id + "_" + category_id +"_matches.json", "w") as file:
            json.dump(parsed, file, ensure_ascii=False, indent=4)

        print("Matches saved to " + event_id + "_" + category_id +"_matches.json")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    event_id = "ironcup-2025"
    category_id = "20"
    main(event_id, category_id)