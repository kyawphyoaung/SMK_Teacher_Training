game_data = [
    ["Alexis",1,19],
    ["Seema",1,29],
    ["Seema",2,44],
    ["Lois",1,10],
    ["Alexis",2,17],
    ["Alexis",3,36],
    ["Dion",1,23],
    ["Emma",1,27],
    ["Emma",2,48]
]

def get_highest_player(level, game_data):
    max_score = 0
    for player in game_data:
        if player[1] == level:
            if player[2] > max_score:
                max_score=player[2]
                highest_player = player
    return highest_player


lvl1_higest_player = get_highest_player(1,game_data)
lvl2_higest_player = get_highest_player(2,game_data)
lvl3_highest_player = get_highest_player(3,game_data)

print(lvl1_higest_player)
print(lvl2_higest_player)
print(lvl3_highest_player)