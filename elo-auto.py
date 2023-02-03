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

def update_ratings(matches):
    ratings = {}
    for match in matches:
        playerWinner, playerLoser = match
        if playerWinner not in ratings:
            ratings[playerWinner] = 1500
        if playerLoser not in ratings:
            ratings[playerLoser] = 1500
        ratings = calculate_elo(playerWinner, playerLoser, ratings)
    return ratings

matches = [
    ## ROBOTO LAB - AUTO
    ('Equipe-Paralela',  'Raiju'           ), 
    ('ThundeRatz',       'KIMAUÁNISSO'     ),
    ('KIMAUÁNISSO',      'Equipe-Paralela' ),
    ('ThundeRatz',       'OMEGABOTZ'       ),
    ('OMEGABOTZ',        'Raiju'           ),
    ('KIMAUÁNISSO',      'Equipe-Paralela' ),
    ('KIMAUÁNISSO',      'ThundeRatz'      ),
    ('KIMAUÁNISSO',      'OMEGABOTZ'       ),
    ('KIMAUÁNISSO',      'ThundeRatz'      ),

    ## RSM - AUTO
    ('KIMAUÁNISSO',      'RobotBulls'  ), 
    ('OMEGABOTZ',        'RobotBulls'  ),
    ('KIMAUÁNISSO',      'OMEGABOTZ'   ),
    ('SIRE-UB',          'KIMAUÁNISSO' ),
    ('Raiju',            'KIMAUÁNISSO' ),
    ('Raiju',            'SIRE-UB'     ),
    ('TRINCABOTZ',       'ThundeRatz'  ),
    ('TRINCABOTZ',       'RobotBulls'  ),
    ('ThundeRatz',       'RobotBulls'  ),
    ('SIRE-UB',          'OMEGABOTZ'   ),
    ('ThundeRatz',       'TRINCABOTZ'  ),
    ('KIMAUÁNISSO',      'SIRE-UB'     ),
    ('Raiju',            'ThundeRatz'  ),
    ('TRINCABOTZ',       'SIRE-UB'     ),
    ('ThundeRatz',       'OMEGABOTZ'   ),
    ('TRINCABOTZ',       'ThundeRatz'  ),
    ('KIMAUÁNISSO',      'Raiju'       ),
    ('Raiju',            'TRINCABOTZ'  ),
    ('KIMAUÁNISSO',      'Raiju'       ),


    ## RoboChallenge - Auto
    ('Raiju',            'MinervaBots'     ), 
    ('Raiju',            'Equipe-Paralela' ),
    ('OMEGABOTZ',        'MinervaBots'     ),
    ('KIMAUÁNISSO',      'OMEGABOTZ'       ),
    ('ThundeRatz',       'RobotBulls'      ),
    ('KIMAUÁNISSO',      'MinervaBots'     ),
    ('KIMAUÁNISSO',      'Raiju'           ),
    ('Equipe-Paralela',  'MinervaBots'     ),
    ('RobotBulls',       'Equipe-Paralela' ),
    ('ThundeRatz',       'KIMAUÁNISSO'     ),
    ('ThundeRatz',       'KIMAUÁNISSO'     ),
    ('Raiju',            'RobotBulls'      ),
    ('KIMAUÁNISSO',      'OMEGABOTZ'       ),
    ('KIMAUÁNISSO',      'ThundeRatz'      ),
    ('KIMAUÁNISSO',      'Raiju'           ),
    ('KIMAUÁNISSO',      'ThundeRatz'      ),
    ('ThundeRatz',       'KIMAUÁNISSO'     ),


    ## Inatel - Auto
    ('FEG-Robótica',       'RobotBulls'    ),
    ('Uai!rrior',          'OMEGABOTZ'     ),
    # ('FEG-Robótica',       'ThundeRatz'    ), Thunder nem foi na competição
    ('RobotBulls',         'UERJBotz'      ),
    ('OMEGABOTZ',          'Phoenix'       ),
    ('RobotBulls',         'OMEGABOTZ'     ),
    ('FEG-Robótica',       'Uai!rrior'     ),
    ('FEG-Robótica',       'TRINCABOTZ'    ),
    ('MinervaBots',        'RobotBulls'    ),
    ('RobotBulls',         'OMEGABOTZ'     ),
    # ('MinervaBots',        'ThundeRatz'    ), Thunder nem foi na competição
    ('TRINCABOTZ',         'UERJBotz'      ),
    ('Phoenix',            'Uai!rrior'     ),
    ('RobotBulls',         'OMEGABOTZ'     ),
    ('RobotBulls',         'MinervaBots'   ),
    ('Phoenix',            'TRINCABOTZ'    ),
    ('OMEGABOTZ',          'RobotBulls'    ),
    ('FEG-Robótica',       'Phoenix'       ),
    ('RobotBulls',         'FEG-Robótica'  ),
    ('OMEGABOTZ',          'FEG-Robótica'  ),
    ('RobotBulls',         'FEG-Robótica'  ),

    #Final dupla
    ('RobotBulls',         'OMEGABOTZ'     ), 
    ('RobotBulls',         'OMEGABOTZ'     ),


    ## RCX - Auto
    ('KIMAUÁNISSO',        'RAS-UFRB'         ),
    ('Equipe-Paralela',    'RobotBulls'       ),
    ('Robótica-TERA',      'TRINCABOTZ'       ),
    ('Sumomasters',        'ThundeRatz'       ),
    ('KIMAUÁNISSO',        'OMEGABOTZ'        ),
    ('RioBotz',            'Sumomasters'      ),
    ('Sumomasters',        'RobotBulls'       ),

    ('RobotBulls',         'RAS-UFRB'         ),
    ('TRINCABOTZ',         'ThundeRatz'       ),
    ('OMEGABOTZ',          'Sumomasters'      ),

    ('Equipe-Paralela',    'KIMAUÁNISSO'      ),
    ('Sumomasters',        'Robótica-TERA'    ),
    ('KIMAUÁNISSO',        'RioBotz'          ),
    ('ThundeRatz',         'Sumomasters'      ),

    ('RobotBulls',         'Sumomasters'      ),
    ('RioBotz',            'TRINCABOTZ'       ),
    ('OMEGABOTZ',          'Robótica-TERA'    ),
    ('KIMAUÁNISSO',        'RobotBulls'       ),

    ('RobotBulls',         'RioBotz'          ),
    ('KIMAUÁNISSO',        'OMEGABOTZ'        ),

    ('Equipe-Paralela',    'Sumomasters'      ),
    ('KIMAUÁNISSO',        'ThundeRatz'       ),

    ('Sumomasters',        'RobotBulls'       ),

    ('Equipe-Paralela',    'KIMAUÁNISSO'      ),

    ('Sumomasters',        'KIMAUÁNISSO'      ),

    #Final dupla
    ('Sumomasters',        'Equipe-Paralela'  ),
    ('Sumomasters',        'Equipe-Paralela'  ),



]

elo_ratings = update_ratings(matches)

for v in sorted( elo_ratings.values(), reverse=True ):
    for key in elo_ratings:
        if elo_ratings[ key ] == v:
            print (str(round(v)) + " - " + key)
            break
