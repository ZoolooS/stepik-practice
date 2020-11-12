'''
Программа принимает на стандартный вход список игр футбольных команд с результатом матчаю
Выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
    Пример:
    3
    Спартак;9;Зенит;10
    Локомотив;12;Зенит;3
    Спартак;8;Локомотив;15

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
    Пример:
    Спартак:2 0 0 2 0
    Зенит:2 1 0 1 3
    Локомотив:2 2 0 0 6

Порядок вывода команд произвольный.
'''
# ====== imports block ================================== #


# ====== function declaration =========================== #
def get_set_of_clubs(games):
    clubs = []
    [clubs.extend(el.keys()) for el in games]
    return set(clubs)


def get_plays(games, club):
    return [club, len([el for el in games if club in el.keys()])]


def get_results(games, club):
    plays = [el for el in games if club in el.keys()]
    wins, draws, loses = 0, 0, 0
    for el in plays:
        if min(*el.values()) == max(*el.values()):
            draws += 1
        elif max(*el.values()) == el[club]:
            wins += 1
        elif min(*el.values()) == el[club]:
            loses += 1
    return [club, wins, draws, loses]


def count_points(results):
    return [[el[0], el[1] * 3 + el[2]] for el in results]


def combine_stats(plays, results, points):
    stats = plays
    
    for el in stats:
        for result in results:
            if el[0] == result[0]:
                el.extend(result[1:])
    
    for el in stats:
        for point in points:
            if el[0] == point[0]:
                el.extend(point[1:])

    return stats


# ====== main code ====================================== #
games_total = int(input())
games = [{el[i]: int(el[i + 1]) for i in range(0, len(el), 2)} for el in [input().split(';') for _ in range(games_total)]]
print('games =>', games)

clubs = get_set_of_clubs(games)
#print('clubs =>', clubs)

plays = [get_plays(games, club) for club in clubs]
#print('plays =>', plays)

results = [get_results(games, club) for club in clubs]
#print('results =>', results)

points = count_points(results)
#print('points =>', points)

stat_table = combine_stats(plays, results, points) 
#print('stat_table =>', *stat_table)
for el in stat_table:
    print(f'{el[0]}:{" ".join(map(str, el[1:]))}')

# ====== end of code ==================================== #