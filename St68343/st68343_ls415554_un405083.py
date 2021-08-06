"""<https://stepik.org/lesson/415554?unit=405083>
"""
# ======================================================= #
def coord_quarters_distribution():
    points_num = int(input())
    points = [[int(coord) for coord in input().split()] for _ in range(points_num)]

    # print(f'points: {points}')

    quarts = [0, 0, 0, 0, 0]

    for point in points:
        if point[0] == 0 or point[1] == 0:
            quarts[0] += 1
        elif point[0] > 0 and point[1] > 0:
            quarts[1] += 1
        elif point[0] < 0 and point[1] > 0:
            quarts[2] += 1
        elif point[0] < 0 and point[1] < 0:
            quarts[3] += 1
        elif point[0] > 0 and point[1] < 0:
            quarts[4] += 1

    print(f'Первая четверть: {quarts[1]}')
    print(f'Вторая четверть: {quarts[2]}')
    print(f'Третья четверть: {quarts[3]}')
    print(f'Четвертая четверть: {quarts[4]}')

# coord_quarters_distribution()

# ======================================================= #
def ascending_counter():
    nums = [int(n) for n in input().split()]
    print(sum(list(map(lambda a, b: b > a, nums[:-1], nums[1:]))))

# ascending_counter()

# ======================================================= #
def swap_by_pair():
    nums = [int(n) for n in input().split()]

    if len(nums) == 1:
        return nums

    for k, v in enumerate(nums):
        if k % 2 == 1:
            nums[k], nums[k - 1] = nums[k - 1], nums[k]
        else:
            continue

    return nums

# print(*swap_by_pair())

# ======================================================= #
def biggest():
    print([215 ** 10, 23 ** 45, 10 ** 215, 45 ** 23])
    print(sorted([215 ** 10, 23 ** 45, 10 ** 215, 45 ** 23]))

# biggest()

# ======================================================= #
def solve_01():
    # print(75 * 3 * 10 ** 16)
    # print((12.349 ** 2 + 147.745 ** 2) ** 0.5)
    # print(2 * 3.14 * (23 / 9.18) ** 0.5)
    # print(6.674 * 10 ** -11 * ((70 * 5.97 * 10 ** 24) / (6371 * 10 ** 3)))
    # print(100500 % 7)
    print(123456789 // 8)
    # print()

# solve_01()

# ======================================================= #
# year = 1

def witch_school(year):
    if year < 5:
        school_type = 'младшая школа'
    elif 5 <= year <= 8:
        school_type = 'средняя школа'
    elif year > 8:
        school_type = 'старшая школа'
    return school_type

# print(witch_school(year))

# ======================================================= #
# values = [5, 10, 2, 11, 12]
# total = 0

# [total := total + v for v in values]
# print("Total:", total)

# print(*(small, large), sep='\n')

# ======================================================= #
def high_years():
    leap_years = []
    [leap_years.append(year) for year in range(2025, 9999) if (not (year % 4) or not (year % 400)) if (year % 100) and len(leap_years) < 20]
    # leap_years = leap_years[:20]
    print(leap_years)
    # [leap_years.del(year) for year in leap_years if year % 400]

# high_years()

# ======================================================= #
# from functools import reduce
# from operator import add, mul
# op = {'sum': 'add()', 'product': 'mul()'}
# # op = {'sum': 'lambda a, b: a + b', 'product': 'lambda a, b: a * b'}
# result = reduce(eval(op[operation]), range(1, n + 1))

# ======================================================= #
# from collections import Counter

# n = int(input())
# chips = [int(el) for el in input().split(' ')]
# k = int(input())

# unics = Counter(chips)
# chips_cut = []
# [chips_cut.extend((key, key)) if val > 1 else chips_cut.append(key) for key, val in unics.items()]
# chips_cut.sort()
# chips_cut = tuple(chips_cut)

def find_pare_by_subtraction(chips, k):
    for key, val in enumerate(chips):
        # if (k - val in set(chips[key + 1:])):
        if (k - val in chips) and (chips.index(k - val) != key):
            return (val, k - val)

    return [None]

def find_pare_by_indexes_slide(chips, k):
    start_idx = 0
    end_idx = -1
    length = len(chips)

    for i in range(length - 1):
        if start_idx - end_idx == length:
            return [None]

        total = chips[start_idx] + chips[end_idx]
        if total == k:
            return (chips[start_idx], chips[end_idx])
        elif total > k:
            # print(f'> {start_idx = }, {end_idx = } | {k = } | {total = }')
            end_idx -= 1
        elif total < k:
            # print(f'< {start_idx = }, {end_idx = } | {k = } | {total = }')
            start_idx += 1

    return [None]


# result = find_pare_by_subtraction(chips_cut, k)  # > 1s 12.61Mb
# result = find_pare_by_indexes_slide(chips_cut, k)  # 140ms 12.79Mb
# print(f'{result = }')
# print(*result)
# print(unics)
# print(f'{chips_cut = }')
# print(*result)
# print(*chips)

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #

# ======================================================= #
