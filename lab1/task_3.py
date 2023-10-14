list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
mid_point = len(list_players) // 2
team1, team2 = list_players[:mid_point], list_players[mid_point:]
print(team1)
print(team2)
