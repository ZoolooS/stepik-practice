def part_with_a():
    marks = input().split()
    print(f'{(marks.count("A") / len(marks)):.2f}')

#part_with_a()

# #=================================================================# #
def decimal_to_roman():
    dec = input()[::-1]
    roman = []

    d2r = {'1': ['I', 'X', 'C', 'M'],
           '2': ['II', 'XX', 'CC', 'MM'],
           '3': ['III', 'XXX', 'CCC', 'MMM'],
           '4': ['IV', 'XL', 'CD'],
           '5': ['V', 'L', 'D'],
           '6': ['VI', 'LX', 'DC'],
           '7': ['VII', 'LXX', 'DCC'],
           '8': ['VIII', 'LXXX', 'DCCC'],
           '9': ['IX', 'XC', 'CM'],
           '0': ['', '', '']}

    [roman.append(d2r[dec[i]][i]) for i in range(len(dec))]
    print(''.join(roman[::-1]))


#decimal_to_roman()

# #=================================================================# #
def length_converter():
    s = input().split()
    l_units = {'mm': 0.001, 'cm': 0.01, 'm': 1, 'km': 1000,
               'inch': 0.0254, 'foot': 0.3048, 'yard': 0.9144, 'mile': 1609}

    print(f'{float(s[0]) * l_units[s[1]] / l_units[s[3]]:.2e}')

#length_converter()

# #=================================================================# #
def some_calculations_001(x: float):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -(x / 2)
    elif 2 < x:
        return (x - 2) ** 2 + 1

#some_calculations_001(x)

# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #


# #=================================================================# #
