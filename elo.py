import sys
import json
import os

# foreign participants don't count on brazilian rankings
foreign_robots = [
    "Masakrator",
    "SIRE-UB",
    "HAKA A",
    "HAKA B",
    "Grigio"
]

foreign_teams = [
    "Sumomasters",
    "SIRE-UB",
    "SIRE-RC-UB",
    "PinoyFlash"
]


def calculate_wins_losses(playerWinner, playerLoser, winsLosses):
    winsLosses[playerWinner][0] += 1
    winsLosses[playerLoser][1] += 1
    return winsLosses

def update_wins_losses(matches, winsLosses):
    for match in matches:
        playerWinner, playerLoser = match
        if playerWinner not in winsLosses:
            winsLosses[playerWinner] = [0,0]
        if playerLoser not in winsLosses:
            winsLosses[playerLoser] = [0,0]
        winsLosses = calculate_wins_losses(playerWinner, playerLoser, winsLosses)
    return winsLosses

def calculate_elo(playerWinner, playerLoser, ratings):
    k = 20
    rating1 = ratings[playerWinner]
    rating2 = ratings[playerLoser]
    expected_score1 = 1 / (1 + 10 ** ((rating2 - rating1) / 400))
    expected_score2 = 1 / (1 + 10 ** ((rating1 - rating2) / 400))

    pointsWinner = k * (1 - expected_score1)
    pointsLoser  = k * (0 - expected_score2)
    
    ratings[playerWinner] = rating1 + pointsWinner
    ratings[playerLoser]  = rating2 + pointsLoser

    return ratings

def update_ratings(matches, ratings):
    for match in matches:
        playerWinner, playerLoser = match
        if playerWinner not in ratings:
            ratings[playerWinner] = 1500
        if playerLoser not in ratings:
            ratings[playerLoser] = 1500
        ratings = calculate_elo(playerWinner, playerLoser, ratings)
    return ratings

def read_competitions(path):

    all_competitions = []

    # Read all .json files from given directory
    for filename in os.listdir(path):
        if filename.endswith(".json"):
            with open(os.path.join(path, filename), "rb") as f:
                data = json.load(f)
                all_competitions.append(data)

    # Sort competition by year
    all_competitions = sorted(all_competitions, key=lambda x: x['year'])
    return all_competitions



def print_ordered(rankings, win_ratio, elo_threshold):
    sorted_items = sorted(rankings.items(), key=lambda x: x[1], reverse=True)
    count = 0
    for item in sorted_items:
        wins = win_ratio[item[0]][0]
        losses = win_ratio[item[0]][1]
        if ((item[0] in (foreign_robots + foreign_teams)) or (wins + losses < elo_threshold)):
            print("|  *  | ", end="")
        else :
            count += 1
            print("| #{:02d} | ".format(count), end="")

        print("{:03d} / {:03d} | {} | {}".format((win_ratio[item[0]][0]), (win_ratio[item[0]][1]), round(item[1]), item[0]))
    print("")


def print_detailed_info(competition_name, year_ratings, complete_ratings, competition_date, year_win_ratio, complete_win_ratio, rating_type):
    print_header(competition_name)
    print_header(competition_date)
    print("\r\nYear Ratings")
    print_ordered(year_ratings, year_win_ratio, 5)
    print("Complete Ratings")
    if (rating_type == "matches-robots"):
        print_ordered(complete_ratings, complete_win_ratio, 8)
    else:
        print_ordered(complete_ratings, complete_win_ratio, 10)

def print_header(header):
    len_header = len(header)
    if (len_header % 2 != 0):
        header += "-"
        len_header += 1
    desired_len = 32
    pad_len = (desired_len - len_header)/2
    pad_string = "-" * int(pad_len)
    print(pad_string + header + pad_string)



def main():

    if len(sys.argv) != 4:
        print('Usage: python3 elo.py <folder_path(auto/rc)> <robot/team> <print_logs(true/false)>')
        sys.exit()

    folder_name = sys.argv[1]
    print_logs = sys.argv[3] == "true"

    rating_type = 'matches'
    if (sys.argv[2] == "robot"):
        rating_type = 'matches-robots'

    all_competitions = read_competitions(folder_name)
    all_matches = []
    complete_ratings = {}
    complete_wins_and_losses = {}
    
    # Calculate Elo for each year, and then calculate a general from all files
    for year_data in all_competitions:
        
        print("--------------------------------")
        print_header(str(year_data["year"]))
        print("--------------------------------\r\n")

        year_competitions = year_data['competitions']['competition']
        year_matches = []
        year_ratings = {}
        year_wins_and_losses = {}

        for competition in year_competitions:
            matches = competition[rating_type]

            year_wins_and_losses = update_wins_losses(matches, year_wins_and_losses)
            complete_wins_and_losses = update_wins_losses(matches, complete_wins_and_losses)
            
            year_matches += matches
            year_ratings = update_ratings(matches, year_ratings)
            
            all_matches += matches
            complete_ratings = update_ratings(matches, complete_ratings)

            if (print_logs):
                print_detailed_info(competition['name'], year_ratings, complete_ratings,
                                    competition['date'], year_wins_and_losses, complete_wins_and_losses, rating_type)

        if (not print_logs):
            print("Complete Ratings\r\n")
            if (rating_type == "matches-robots"):
                print_ordered(complete_ratings, complete_wins_and_losses, 8)
            else:
                print_ordered(complete_ratings, complete_wins_and_losses, 10)




if __name__ == '__main__':
    main()