import sys
import json
import math

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

    # print(playerWinner + " + " + str(round(pointsWinner)))
    # print(playerLoser + " - " + str(round(pointsWinner)))
    # print("")


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

def read_competitions(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    competitions = data['competitions']['competition']
    return competitions


def print_ordered(rankings):
    for v in sorted( rankings.values(), reverse=True ):
            for key in rankings:
                if rankings[ key ] == v:
                    print (str(round(v)) + " - " + key)
                    break
    print("")


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 myProgram.py <matches_file>')
        sys.exit()

    file_name = sys.argv[1]
    competitions = read_competitions(file_name)

    all_matches = []
    all_matches_ratings = {}

    for competition in competitions:
        
        # Current competition
        print(competition['name'])
        matches = competition['matches']
        ratings = {}
        elo_ratings = update_ratings(matches, ratings)
        # print_ordered(elo_ratings)

        # All competitions
        print("all_matches")
        all_matches += matches
        all_matches_ratings = update_ratings(matches, all_matches_ratings)
        print_ordered(all_matches_ratings)


if __name__ == '__main__':
    main()