import math

def calculate_elo(player1, player2, result, ratings):
    k = 20
    rating1 = ratings[player1]
    rating2 = ratings[player2]
    expected_score1 = 1 / (1 + 10 ** ((rating2 - rating1) / 400))
    expected_score2 = 1 / (1 + 10 ** ((rating1 - rating2) / 400))
    if result == 'win':
        ratings[player1] = rating1 + k * (1 - expected_score1)
        ratings[player2] = rating2 + k * (0 - expected_score2)
    elif result == 'lose':
        ratings[player1] = rating1 + k * (0 - expected_score1)
        ratings[player2] = rating2 + k * (1 - expected_score2)
    else:
        ratings[player1] = rating1 + k * (0.5 - expected_score1)
        ratings[player2] = rating2 + k * (0.5 - expected_score2)
    return ratings

def update_ratings(matches):
    ratings = {}
    for match in matches:
        player1, player2, result = match
        if player1 not in ratings:
            ratings[player1] = 1500
        if player2 not in ratings:
            ratings[player2] = 1500
        ratings = calculate_elo(player1, player2, result, ratings)
    return ratings

matches = [
    ## ROBOTO LAB - AUTO
    ('Equipe-Paralela',  'Raiju',             'win'), 
    ('ThundeRatz',       'KIMAUÁNISSO',       'win'),
    ('KIMAUÁNISSO',      'Equipe-Paralela',   'win'),
    ('ThundeRatz',       'OMEGABOTZ',         'win'),
    ('OMEGABOTZ',        'Raiju',             'win'),
    ('KIMAUÁNISSO',      'Equipe-Paralela',   'win'),
    ('KIMAUÁNISSO',      'ThundeRatz',        'win'),
    ('KIMAUÁNISSO',      'OMEGABOTZ',         'win'),
    ('KIMAUÁNISSO',      'ThundeRatz',        'win'),

    ## RSM - AUTO
    ('KIMAUÁNISSO',      'RobotBulls',    'win'), 
    ('OMEGABOTZ',        'RobotBulls',    'win'),
    ('KIMAUÁNISSO',      'OMEGABOTZ',     'win'),
    ('SIRE-UB',          'KIMAUÁNISSO',   'win'),
    ('Raiju',            'KIMAUÁNISSO',   'win'),
    ('Raiju',            'SIRE-UB',       'win'),
    ('TRINCABOTZ',       'ThundeRatz',    'win'),
    ('TRINCABOTZ',       'RobotBulls',    'win'),
    ('ThundeRatz',       'RobotBulls',    'win'),
    ('SIRE-UB',          'OMEGABOTZ',     'win'),
    ('ThundeRatz',       'TRINCABOTZ',    'win'),
    ('KIMAUÁNISSO',      'SIRE-UB',       'win'),
    ('Raiju',            'ThundeRatz',    'win'),
    ('TRINCABOTZ',       'SIRE-UB',       'win'),
    ('ThundeRatz',       'OMEGABOTZ',     'win'),
    ('TRINCABOTZ',       'ThundeRatz',    'win'),
    ('KIMAUÁNISSO',      'Raiju',         'win'),
    ('Raiju',            'TRINCABOTZ',    'win'),
    ('KIMAUÁNISSO',      'Raiju',         'win'),


    ## RoboChallenge - Auto
    ('Raiju',            'MinervaBots',        'win'), 
    ('Raiju',            'Equipe-Paralela',    'win'),
    ('OMEGABOTZ',        'MinervaBots',        'win'),
    ('KIMAUÁNISSO',      'OMEGABOTZ',          'win'),
    ('ThundeRatz',       'RobotBulls',         'win'),
    ('KIMAUÁNISSO',      'MinervaBots',        'win'),
    ('KIMAUÁNISSO',      'Raiju',              'win'),
    ('Equipe-Paralela',  'MinervaBots',        'win'),
    ('RobotBulls',       'Equipe-Paralela',    'win'),
    ('ThundeRatz',       'KIMAUÁNISSO',        'win'),
    ('ThundeRatz',       'KIMAUÁNISSO',        'win'),
    ('Raiju',            'RobotBulls',         'win'),
    ('KIMAUÁNISSO',      'OMEGABOTZ',          'win'),
    ('KIMAUÁNISSO',      'ThundeRatz',         'win'),
    ('KIMAUÁNISSO',      'Raiju',              'win'),
    ('KIMAUÁNISSO',      'ThundeRatz',         'win'),
    ('ThundeRatz',       'KIMAUÁNISSO',        'win'),


    ## Inatel - Auto
    ('FEG-Robótica',            'RobotBulls',          'win'),
    ('Uai!rrior',               'OMEGABOTZ',           'win'),
    ('FEG-Robótica',            'ThundeRatz',          'win'),
    ('RobotBulls',              'UERJBotz',            'win'),
    ('OMEGABOTZ',               'Phoenix',             'win'),
    ('KIMAUÁNISSO',             'Raiju',               'win'),
    ('KIMAUÁNISSO',             'ThundeRatz',          'win'),
    ('ThundeRatz',              'KIMAUÁNISSO',         'win'),
    ('RobotBulls',              'OMEGABOTZ',           'win'),
    ('FEG-Robótica',            'Uai!rrior',           'win'),
    ('FEG-Robótica',            'TRINCABOTZ',          'win'),
    ('MinervaBots',             'RobotBulls',          'win'),
    ('RobotBulls',              'OMEGABOTZ',           'win'),
    ('MinervaBots',             'ThundeRatz',          'win'),
    ('TRINCABOTZ',              'UERJBotz',            'win'),
    ('Phoenix',                 'Uai!rrior',           'win'),
    ('RobotBulls',              'OMEGABOTZ',           'win'),
    ('RobotBulls',              'MinervaBots',         'win'),
    ('Phoenix',                 'TRINCABOTZ',          'win'),
    ('OMEGABOTZ',               'RobotBulls',          'win'),
    ('FEG-Robótica',            'Phoenix',             'win'),
    ('RobotBulls',              'FEG-Robótica',        'win'),
    ('OMEGABOTZ',               'FEG-Robótica',        'win'),
    ('RobotBulls',              'FEG-Robótica',        'win'),
    ('RobotBulls',              'OMEGABOTZ',           'win'), ##Final dupla
    ('RobotBulls',              'OMEGABOTZ',           'win'),


    ## RCX - Auto
    ('KIMAUÁNISSO',            'RAS-UFRB',                  'win'),
    ('Equipe-Paralela',        'RobotBulls',                'win'),
    ('Robótica-TERA',          'TRINCABOTZ',                'win'),
    ('Sumomasters',            'ThundeRatz',                'win'),
    ('KIMAUÁNISSO',            'OMEGABOTZ',                 'win'),
    ('RioBotz',                'Sumomasters',               'win'),
    ('Sumomasters',            'RobotBulls',                'win'),

    ('RobotBulls',             'RAS-UFRB',                  'win'),
    ('TRINCABOTZ',             'ThundeRatz',                'win'),
    ('OMEGABOTZ',              'Sumomasters',               'win'),

    ('Equipe-Paralela',        'KIMAUÁNISSO',               'win'),
    ('Sumomasters',            'Robótica-TERA',             'win'),
    ('KIMAUÁNISSO',            'RioBotz',                   'win'),
    ('ThundeRatz',             'Sumomasters',               'win'),

    ('RobotBulls',             'Sumomasters',               'win'),
    ('RioBotz',                'TRINCABOTZ',                'win'),
    ('OMEGABOTZ',              'Robótica-TERA',             'win'),
    ('KIMAUÁNISSO',            'RobotBulls',                'win'),

    ('RobotBulls',             'RioBotz',                   'win'),
    ('KIMAUÁNISSO',            'OMEGABOTZ',                 'win'),

    ('Equipe-Paralela',        'Sumomasters',               'win'),
    ('KIMAUÁNISSO',            'ThundeRatz',                'win'),

    ('Sumomasters',            'RobotBulls',                'win'),

    ('Equipe-Paralela',        'KIMAUÁNISSO',               'win'),

    ('Sumomasters',            'KIMAUÁNISSO',               'win'),

    ##Final  dupla
    ('Sumomasters',             'Equipe-Paralela',           'win'),
    ('Sumomasters',             'Equipe-Paralela',           'win'),



]

elo_ratings = update_ratings(matches)

for v in sorted( elo_ratings.values(), reverse=True ):
    for key in elo_ratings:
        if elo_ratings[ key ] == v:
            print (str(round(v)) + " - " + key)
            break
