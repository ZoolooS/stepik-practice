from typing import Counter


def shout_numbers_of_programmers():
    proggers = int(input())

    if ((proggers % 10) == 0) or (5 <= (proggers % 10) <= 9) or (11 <= (proggers % 100) <= 19):
        print(proggers, 'программистов')
    elif (proggers % 10) == 1:
        print(proggers, 'программист')
    elif (2 <= (proggers % 10) <= 4) :
        print(proggers, 'программиста')

##===================================================================##
def is_ticket_lucky(ticket):

    print(len(str(int(ticket))))

    if len(str(int(ticket))) == 5:
        number = int(ticket)
        dig1 = 0
        dig6 = number % 10
        dig5 = (number // 10) % 10
        dig4 = ((number // 10) // 10) % 10
        dig3 = (((number // 10) // 10) // 10) % 10
        dig2 = ((((number // 10) // 10) // 10) // 10) % 10
    else:
        number = int(ticket)
        dig6 = number % 10
        dig5 = (number // 10) % 10
        dig4 = ((number // 10) // 10) % 10
        dig3 = (((number // 10) // 10) // 10) % 10
        dig2 = ((((number // 10) // 10) // 10) // 10) % 10
        dig1 = (((((number // 10) // 10) // 10) // 10) // 10) % 10
    
    #number = int(number) #int(input())
    #print(dig1, dig2, dig3, dig4, dig5, dig6)

    sum1 = dig1 + dig2 + dig3
    sum2 = dig4 + dig5 + dig6
    #print(sum1)
    #print(sum2)

    if sum1 == sum2:
        print('Счастливый')
    else:
        print('Обычный')

#is_ticket_lucky('090234')

##===================================================================##
def simple_cycle():
    i = 0
    counter = 0
    while i <= 10:
        i = i + 1
        if i > 7:
            i = i + 2
        counter += 1
    
    print(i)
    print(counter)

#simple_cycle()

##===================================================================##
def print_stars():
    i = 0
    while i < 5:
        print('*')
        if i % 2 == 0:
            print('**')
        if i > 2:
            print('***')
        i = i + 1

#print_stars()

##===================================================================##
def input_summator():
    sum = 0
    dig = 1
    while dig != 0:
        dig = int(input())
        print('sum =', sum)
        #num = int(input())
        sum += dig
    print('Итог:', sum)

#input_summator()

##===================================================================##
def min_pie_cutter():
    a = int(input())
    b = int(input())

    devider = 2
    nod = 1
    #min_pieces = 1

    # Находим НОД
    while (devider <= a) or (devider <= b):
        if (a % devider == 0) and (b % devider == 0):
            nod = devider
        devider += 1

    nok = (a * b) / nod

    print(int(nok))

#min_pie_cutter()

##===================================================================##
def range_printer():
    while True:
        number = int(input())

        if number < 10:
            continue
        if number > 100:
            break

        print(number)

#range_printer()

##===================================================================##
def pifagor_table():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    '''if (0 > a,b,c,d > 10) or (a > b) or (c > d):
        print('Что-то пошло не так!')
        #return'''

    for j in range(c, d + 1):
        print('\t' + str(j), end='')
    print()

    for i in range(a, b + 1):
        print(str(i), end='')
        for k in range(c, d + 1):
            mult = i * k
            print('\t' + str(mult), end='')
        print()

#pifagor_table()

##===================================================================##
def average():
    a = int(input())
    b = int(input())
    devider = 3
    counter = 0
    sum = 0

    for k in range(a, b + 1):
        if k % devider == 0:
            sum += k
            counter += 1

    average_sum = sum / counter

    print(average_sum)

#average()
##===================================================================##
def string_counter():
    dna_string = str(input())
    dna_string = dna_string.upper()
    nuk_sign1 = 'G'
    nuk_sign2 = 'C'

    counter_sign1 = dna_string.count(nuk_sign1)
    counter_sign2 = dna_string.count(nuk_sign2)

    proc = (counter_sign1 + counter_sign2) / len(dna_string) * 100

    print(proc)

''' Другой вариант
s = input().upper()
print((s.count('G') + s.count('C'))/len(s) * 100)
'''

#string_counter()

##===================================================================##
def is_palindrome():
    s = input()
    if s == s[::-1]:
        print(s, 'палиндром')
    else:
        print(s, 'не палиндром')


#is_palindrome()

##===================================================================##
''' Выборки из строки
s = 'abcdefghijk'
print(s[3:6], s[:6], s[3:], s[::-1], s[-3:], s[:-6], s[-1:-10:-2])
'''

##===================================================================##
def gen_encoder():
    s = input()
    s_en = s[0]
    i = 1
    counter = 1

    while i < len(s):
        if s[i] == s[i-1]:
            counter += 1
        else:
            s_en += str(counter) + s[i]
            if i - 1 == len(s):
                break
            counter = 1
        i += 1

    s_en += str(counter)

    print(s_en)

#def gen_encoder()

##===================================================================##
def summator():
    s = [int(i) for i in input().split()]

    j = 0
    sum = 0

    while j < len(s):
        sum += s[j]
        j += 1

    print(sum)

#summator()

##===================================================================##
def around_summator():
    s = [int(i) for i in input().split()]

    j = 0
    sum = 0

    while j < len(s):
        if len(s) == 1:
            print(s[0])
            break
        elif j + 1 == len(s):
            sum = s[j - 1] + s[0]
            print(sum)
            break #j += 1
        else:
            sum = s[j - 1] + s[j + 1]
            print(sum, end=' ')
            j += 1

#def around_summator()

##===================================================================##
def print_plural():
    s = [int(i) for i in input().split()]

    s_cut = []

    for el in s:
        if s.count(el) > 1:
            if el not in s_cut:
                s_cut.append(el)

    print(*s_cut)

# 5 5 5 5 77 8 95 100 100 5 4 4 6 77 2 3 6 44 44 44

#def print_plural()

##===================================================================##
def miner_game_field_setuper():
    n, m, k = (int(i) for i in input().split())
    a = [[0 for j in range(m)] for i in range(n)]
    for i in range(k):
        row, col = (int(i) - 1 for i in input().split())
        a[row][col] = -1
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                for _ in range(-1, 2):  #di => _
                    for dj in range(-1, 2):
                        ai = i + dj
                        aj = j + dj
                        # (ai, aj)
                        if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                            a[i][j] += 1
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                print('*', end='')
            elif a[i][j] == 0:
                print('.', end='')
            else:
                print(a[i][j], end='')
        print()

#miner_game_field_setuper()

##===================================================================##
def cicles_test_001():
    flag = -1
    total = 0
    total_sqr = 0

    while flag != 0:
        n = int(input())
        total += n
        total_sqr += n ** 2
        if total == 0:
            flag = 0

    print(total_sqr)

#cicles_test_001()

##===================================================================##
def numbers_of_numbers_line():
    n = int(input())
    count = 0
    flag = 0

    for i in range(1, n + 1):
        for _ in range(i):
            count += 1
            if count <= n:
                print(i, end=' ')
            else:
                flag = -1
                break
        if flag == -1:
            break

#numbers_of_numbers_line()

##===================================================================##
def positions_of_digits():
    lst = [int(i) for i in input().split()]
    x = int(input())

    if x not in lst:
        print('Отсутствует')
    else:
        for i in range(len(lst)):
            if lst[i] == x:
                print(i, end=' ')

#positions_of_digits()

##===================================================================##
def generate_matrix_from_matrix():
    matrix = []
    row = []
    result_row = []

    while row != ['end']:
        row = [i for i in input().split()]
        matrix.append(row)

    matrix = matrix[:-1]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result_row.append(int(matrix[i][j - 1]) + int(matrix[i][(j + 1) % len(matrix[i])]) + int(matrix[i - 1][j]) + int(matrix[(i + 1) % len(matrix)][j]))
        print(*result_row)
        result_row = []

#generate_matrix_from_matrix()

##===================================================================##
def spiral_numbers_printer():
    n = int(input())
    n_list = [[0 for i in range(n)] for j in range(n)]
    n_set = [i for i in range(1, n ** 2 + 1)]
    counter = 0

    for circle in range(n // 2):
        #print('circle = ', circle)
        
        # top row
        for row_f in range(circle, n - 1 - circle):
            #print(f'row_f = {row_f} | counter = {counter}')
            n_list[circle][row_f] = n_set[counter]
            counter += 1
            if counter == n ** 2:
                break
        
        # last col
        for col_l in range(circle, n - 1 - circle):
            #print(f'col_l = {col_l} | counter = {counter}')
            n_list[col_l][n - 1 - circle] = n_set[counter]
            counter += 1
            if counter == n ** 2:
                break
        
        # last row
        for row_l in range(n - 1 - circle, circle, - 1):
            #print(f'row_l = {row_l} | counter = {counter}')
            n_list[n - 1 - circle][row_l] = n_set[counter]
            counter += 1
            if counter == n ** 2:
                break
        
        # first col
        for col_f in range(n - 1 - circle, circle, - 1):
            #print(f'col_f = {col_f} | counter = {counter}')
            n_list[col_f][circle] = n_set[counter]
            counter += 1
            if counter == n ** 2:
                break
        
    if n % 2 == 1:
        n_list[n // 2][n // 2] = n_set[-1]

    #print('n_list = ', n_list)
    #print(*n_list, sep='\n')
    for i in range(len(n_list)):
        print(*n_list[i])

#spiral_numbers_printer()

##===================================================================##
def spiral_numbers_printer_alt():
    n = int(input())
    n_list = [[0 for i in range(n)] for j in range(n)]
    counter = 1

    for circle in range(n // 2):

        # top row
        for row_f in range(circle, n - 1 - circle):
            n_list[circle][row_f] = counter
            counter += 1
            if counter == n ** 2:
                break

        # last col
        for col_l in range(circle, n - 1 - circle):
            n_list[col_l][n - 1 - circle] = counter
            counter += 1
            if counter == n ** 2:
                break

        # last row
        for row_l in range(n - 1 - circle, circle, - 1):
            n_list[n - 1 - circle][row_l] = counter
            counter += 1
            if counter == n ** 2:
                break

        # first col
        for col_f in range(n - 1 - circle, circle, - 1):
            n_list[col_f][circle] = counter
            counter += 1
            if counter == n ** 2:
                break

    if n % 2 == 1:
        n_list[n // 2][n // 2] = n ** 2

    for i in range(len(n_list)):
        print(*n_list[i])

#spiral_numbers_printer_alt()

##===================================================================##
def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    if -2 < x <= 2:
        return -(x / 2)
    if x > 2:
        return (x - 2) ** 2 + 1
##===================================================================##
def modify_list(l):
    while [l.pop(l.index(el)) for el in l if el % 2 == 1] != []:
        continue
    l[:] = [el // 2 for el in l]

'''
lst1 = [1, 2, 3, 4, 5, 6]
modify_list(lst1)
print('lst1_01 = ', lst1)
modify_list(lst1)
print('lst1_02 = ', lst1)
lst2 = [10, 5, 8, 3]
modify_list(lst2)
print('lst2 = ', lst2)
lst3 = [0, 5, 8, 0]
modify_list(lst3)
print('lst3 = ', lst3)
lst4 = [1, 3, 5, 7, 9, 11]
modify_list(lst4)
print('lst4 = ', lst4)
'''

##===================================================================##
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        if 2 * key in d:
            d[2 * key].append(value)
        else:
            d[2 * key] = [value]

'''
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
'''

##===================================================================##
def word_counter(str):
    str_list = input().lower().split(' ')
    result = {}

    for el in str_list:
        if el not in result:
            result[el] = 1
        else:
            result[el] += 1

    for el in result:
        print(el, result[el])

#word_counter(str)

##===================================================================##
def result_printer_without_repears():
    n = int(input())
    n_dict = {}
    for _ in range(n):
        x = int(input())
        if x not in n_dict:
            n_dict[x] = f(x)  # f(x) существует вне задания
            print(n_dict[x])
        else:
            print(n_dict[x])

##===================================================================##
def return_run_args():
    from sys import argv

    print(*argv[1:])

#return_run_args()

##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##


##===================================================================##
