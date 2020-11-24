'''a = 100
print('a=', a)
b = a
print('b=', b)

a = 200
print('new b=', b)'''

##===================================================================##
'''n = int(input())

if 999 < n <= 9999 and (n % 7 == 0 or n % 17 == 0):
    print('YES')
else:
    print('NO')'''

##===================================================================##
'''a = int(input())
b = int(input())
c = int(input())

if a + b > c or a + c > b or b + c > a:
    print('YES')
else:
    print('NO')'''

##===================================================================##
'''a = int(input())
b = int(input())
c = int(input())

if a >= b:
    maximum = a
    minimum = b
    middle = c
else:
    maximum = b
    minimum = a
    middle = c

if maximum >= c:
    minimum = b
    middle = c
else:
    maximum = c
    minimum = a
    middle = c

if middle >= minimum:
    None
else:
    middle, minimum = minimum, middle

if minimum + middle > maximum:
    print('YES')
else:
    print('NO')'''

##===================================================================##
'''year = int(input())

if (year % 4 == 0 and not (year % 100 == 0)) or (year % 400 == 0):
    print('YES')
else:
    print('NO')'''

##===================================================================##
#a, b, c = int(input()), int(input()), int(input())

##===================================================================##
def what_color():
    n = int(input())

    if 0 <= n <= 36:
        if n == 0:
            print('зеленый')
        elif (1 <= n <= 10 and n % 2 == 0) or (11 <= n <= 18 and n % 2 == 1) or (19 <= n <= 28 and n % 2 == 0) or (29 <= n <= 36 and n % 2 == 1):
            print('черный')
        else:
            print('красный')
    else:
        print('ошибка ввода')

#what_color()

##===================================================================##
def intersection():
    a1, b1 = int(input()), int(input())
    a2, b2 = int(input()), int(input())

    if b1 < a2 or a1 > b2:
        print('пустое множество')
    elif b1 == a2:
        print(b1)
    elif a1 == b2:
        print(a1)
    elif b1 <= b2 and a1 <= a2:
        print(a2, b1)
    elif b1 >= b2 and a1 >= a2:
        print(a1, b2)
    elif a1 >= a2 and b2 >= b1:
        print(a1, b1)
    elif a1 <= a2 and b2 <= b1:
        print(a2, b2)

#intersection()

##===================================================================##
def is_color_same():
    col1, row1 = int(input()), int(input())
    col2, row2 = int(input()), int(input())

    if (col1 % 2 == 1 and row1 % 2 == 1) or (col1 % 2 == 0 and row1 % 2 == 0):
        color1 = 'white'
    else:
        color1 = 'black'

    if (col2 % 2 == 1 and row2 % 2 == 1) or (col2 % 2 == 0 and row2 % 2 == 0):
        color2 = 'white'
    else:
        color2 = 'black'

    if color1 == color2:
        print('YES')
    else:
        print('NO')

#is_color_same()

##===================================================================##
def is_good_for_team():
    age = int(input())
    sex = input()

    if 10 <= age <= 15 and sex == 'f':
        print('YES')
    else:
        print('NO')

#is_good_for_team()

##===================================================================##
def convert_to_romanian_number():
    n = int(input())

    if 1 <= n <= 10:
        if 1 <= n <= 3:
            print('I' * n)
        elif n == 4:
            print('IV')
        elif 5 <= n <= 8:
            print('V', 'I' * (n - 5), sep='')
        elif n == 9:
            print('IX')
        elif n == 10:
            print('X')
    else:
        print('ошибка')

#convert_to_romanian_number()

##===================================================================##
'''n = int(input())

if n % 2 == 1:
    print('YES')
else:
    if 2 <= n <= 5:
        print('NO')
    elif 6 <= n <= 20:
        print('YES')
    if n > 20:
        print('NO')'''

##===================================================================##
def officer_steps():
    col1, row1 = int(input()), int(input())
    col2, row2 = int(input()), int(input())

    if (col2 - col1 == row2 - row1) or (col2 - col1 == -(row2 - row1)):
        print('YES')
    else:
        print('NO')

#officer_steps()

##===================================================================##
def horse_steps():
    col1, row1 = int(input()), int(input())
    col2, row2 = int(input()), int(input())

    if ((col2 - col1 == 1) and (row2 - row1 == 2)) or ((col2 - col1 == 2) and (row2 - row1 == 1)):
        print('YES')
    elif ((col2 - col1 == -1) and (row2 - row1 == 2)) or ((col2 - col1 == 2) and (row2 - row1 == -1)):
        print('YES')
    elif ((col2 - col1 == -1) and (row2 - row1 == -2)) or ((col2 - col1 == -2) and (row2 - row1 == -1)):
        print('YES')
    elif ((col2 - col1 == 1) and (row2 - row1 == -2)) or ((col2 - col1 == -2) and (row2 - row1 == 1)):
        print('YES')
    else:
        print('NO')

#horse_steps()

##===================================================================##
def queen_steps():
    col1, row1 = int(input()), int(input())
    col2, row2 = int(input()), int(input())

    if (col2 - col1 == row2 - row1) or (col2 - col1 == -(row2 - row1)) or (col2 == col1 or row2 == row1):
        print('YES')
    else:
        print('NO')

#queen_steps()
 
##===================================================================##
'''s = float(input())
v1, v2 = float(input()), float(input())

print(s / (v1 + v2))

a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
min(a, b, c, d, e)
max(a, b, c, d, e)
'''

##===================================================================##
def arrange_numers():
    a, b, c = int(input()), int(input()), int(input())
    print(max(a, b, c))
    print((a + b + c) - (min(a, b, c) + max(a, b, c)))
    print(min(a, b, c))

#arrange_numers()

##===================================================================##
def is_number_interesting():
    '''
    Назовем число интересным, если в нем разность максимальной
    и минимальной цифры равняется средней по величине цифре.
    '''
    n = int(input())

    n1 = n // 100
    n2 = (n // 10) % 10
    n3 = n % 10

    n_max = max(n1, n2, n3)
    n_min = min(n1, n2, n3)
    n_mid = (n1 + n2 + n3) - (n_max + n_min)

    if abs(n_max - n_min) == n_mid:
        print('Число интересное')
    else:
        print('Число неинтересное')

#is_number_interesting()

##===================================================================##
def sum_of_abs():
    a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())

    print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))

#sum_of_abs()

##===================================================================##
def manhattan_path():
    p1, p2 = int(input()), int(input())
    q1, q2 = int(input()), int(input())

    print(abs(p1 - q1) + abs(p2 - q2))

#manhattan_path()

##===================================================================##
#from math import sqrt
#from math import *

#print(int(27 ** (1 / 3)))

##===================================================================##
def evclid_path():
    from math import sqrt

    x1, y1 = float(input()), float(input())
    x2, y2 = float(input()), float(input())

    print(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

#evclid_path()

##===================================================================##
def circle_parametrs():
    import math

    r = float(input())

    print(math.pi * r ** 2)
    print(2 * math.pi * r)

#circle_parametrs()

##===================================================================##
def middle_of():
    import math

    a, b = float(input()), float(input())

    print((a + b) / 2)  # среднее арифметическое
    print(math.pow(a * b, 1 / 2))  # среднее геометрическое
    print(2 * (a * b) / (a + b))  # среднее гармоническое
    print(math.sqrt((a ** 2 + b ** 2) / 2))  # среднее квадратичное

#middle_of()

##===================================================================##
def trigonometry_test_001():
    from math import radians, sin, cos, tan

    '''
    r = x * pi / 180  # перевод из x градусов в r радиан
    '''

    x = float(input())
    r = radians(x)

    print(sin(r) + cos(r) + tan(r) ** 2)

#trigonometry_test_001()

##===================================================================##
def math_func_test_001():
    from math import ceil, floor

    x = float(input())

    print(ceil(x) + floor(x))

#math_func_test_001()

##===================================================================##
def quadratic_equation():
    from math import sqrt

    a, b, c = float(input()), float(input()), float(input())

    disc = b ** 2 - 4 * a * c

    if disc < 0:
        print('Нет корней')
    elif disc == 0:
        print(-(b / (2 * a)))
    else:
        x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print(min(x1, x2))
        print(max(x1, x2))

#quadratic_equation()

##===================================================================##
def area_of_figure():
    from math import tan, pi
    '''
    S = na^2 / 4tan(pi/n)  # площадь правильного многоугольника, где а - длина стороны, n - количество сторон
    '''
    n = int(input())
    a = float(input())

    #s = (n * a ** 2) / (4 * tan(pi / n))

    print((n * a ** 2) / (4 * tan(pi / n)))

#area_of_figure()

##===================================================================##
def range_test_001():
    m, n = int(input()), int(input())

    if m < n:
        for i in range(m, n + 1):
            print(i)
    else:
        for i in range(m, n - 1, -1):
            print(i)

#range_test_001()

##===================================================================##
def range_test_002():
    m, n = int(input()), int(input())  # m > n

    '''
    Вывести нечётные от m до n в порядке убывания
    '''

    # Variant 1
    if m % 2 == 0:
        for i in range(m - 1, n - 1, -2):
            print(i)
    else:
        for i in range(m, n - 1, -2):
            print(i)

    # Variant 2
    for i in range(m, n - 1, -1):
        if i % 2 == 1:
            print(i)

    # Variant 32
    start = (m - 1) // 2 * 2 + 1
    for i in range(start, n - 1, -2):
        print(i)

#range_test_002()

##===================================================================##
def range_test_003():
    m, n = int(input()), int(input())  # m <= n

    for i in range(m, n + 1):
        if (i % 17 == 0) or (i % 3 == 0 and i % 5 == 0) or (i % 10 == 9):
            print(i)

#range_test_003()

##===================================================================##
def multiply_table():
    n = int(input())

    for i in range(1, 11):
        print(n, 'x', i, '=', n * i)

#multiply_table()

##===================================================================##
def is_simple():  # is_prime()
    num = int(input())
    flag = True

    for i in range(2, num):
        if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
            flag = False

    if flag == True:
        print('Число простое')
    else:
        print('Число составное')

#is_simple()

##===================================================================##
def cicles_test_001():
    n = int(input())
    total = 0

    for i in range(1, n + 1):
        if (i ** i) % 10 == 5:
            total += i
        """elif (i ** i) % 10 == 2:
            total += i
        elif (i ** i) % 10 == 8:
            total += i"""
            
    print(total)

#cicles_test_001():

##===================================================================##
def sum_of_deviders():
    n = int(input())
    total = 0

    for i in range(1, n + 1):
        if n % i == 0:
            total += i
            
    print(total)

#sum_of_deviders()

##===================================================================##
def cicles_test_002():
    n = int(input())
    total = 0

    for i in range(1, n + 1):
        total += pow(-1, i + 1) * i

    print(total)

#cicles_test_002()

##===================================================================##
def two_biggest_numbers():
    n = int(input())
    m_max = 0
    m_sec = 0

    for _ in range(0, n):
        m = int(input())
        if m_max <= m:
            m_sec = m_max
            m_max = m
        else:
            if m_sec <= m:
                m_sec = m

    print(m_max)
    print(m_sec)

#two_biggest_numbers()

##===================================================================##
def is_all_even():
    flag = 'YES'
    for _ in range(10):
        if int(input()) % 2 != 0:
            flag = 'NO'
            break

    print(flag)

#is_all_even()

##===================================================================##
def fibonachi_001():
    n = int(input())
    a, b = 0, 1

    for _ in range(n):
        print(b, end=' ')
        a, b = b, a + b

#fibonachi_001()

##===================================================================##
def print_by_digit_001():
    n = int(input())

    while n != 0:
        print(n % 10)
        n //= 10

#print_by_digit_001()

##===================================================================##
def reverse_printer():
    n = int(input())

    while n != 0:
        print(n % 10, end='')
        n //= 10

#reverse_printer()

##===================================================================##
def return_minmax_digits():
    n = int(input())
    minimal, maximal = 9, 0

    while n != 0:
        if minimal > n % 10:
            minimal = n % 10
        if maximal < n % 10:
            maximal = n % 10
        n //= 10

    print('Максимальная цифра равна', maximal)
    print('Минимальная цифра равна', minimal)

#return_minmax_digits()

##===================================================================##
def digit_stats():
    n = int(input())
    n_proc = n
    total_s = 0
    total_m = 1
    counter = 0

    while n_proc % 10 != 0:
        total_s += n_proc % 10
        total_m *= n_proc % 10
        counter += 1
        n_proc //= 10

    print(total_s)
    print(counter)
    print(total_m)
    print(total_s / counter)
    print(n // (10 ** (counter - 1)))
    print(n // (10 ** (counter - 1)) + n % 10)

#digit_stats()

##===================================================================##
def second_digit():
    n_proc = n = int(input())
    counter = 1

    while n_proc // 10 != 0:
        counter += 1
        n_proc //= 10

    print('counter = ', counter)
    x = n // (10 ** (counter - 2))
    print(x % 10)

#second_digit()

##===================================================================##
def is_digits_same():
    n = int(input())
    flag = 'YES'
    last = n % 10

    while n != 0:
        if last == n % 10:
            n //= 10
        else:
            flag = 'NO'
            break
        
    print(flag)

#is_digits_same()

##===================================================================##
def is_digits_ordered():
    n = int(input())
    flag = 'YES'
    last = n % 10

    while n != 0:
        if last <= n % 10:
            last = n % 10
            n //= 10
        else:
            flag = 'NO'
            break
        
    print(flag)

#is_digits_ordered()

##===================================================================##
def min_devider():
    n = int(input())
    devider = 2

    while devider <= n:
        if n % devider == 0:
            break
        else:
            devider += 1

    print(devider)

#min_devider()

##===================================================================##
def print_range_with_excludes():
    n = int(input())

    for i in range(1, n + 1):
        if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
            continue
        else:
            print(i)

#print_range_with_excludes()

##===================================================================##
def some_review_001():
    '''
    На обработку поступает последовательность из 10 целых чисел.
    Известно, что вводимые числа по абсолютной величине не превышают 10^6.
    Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности
    и их произведение.
    Если неотрицательных чисел нет, требуется вывести на экран «NO».
    '''
    count = 0
    production = 1
    for _ in range(1, 11):
        x = int(input())
        if x >= 0:
            production *= x
            count += 1
    if count > 0:
        print(count)
        print(production)
    else:
        print('NO')

#some_review_001()

##===================================================================##
def some_review_002():
    '''
    На обработку поступает последовательность из 10 целых чисел.
    Известно, что вводимые числа по абсолютной величине не превышают 10^6.
    Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности
    и максимальное отрицательное число в последовательности.
    Если отрицательных чисел нет, требуется вывести на экран «NO».
    '''
    total = 0
    x_max = -(10**6) 

    for _ in range(10):
        x = int(input())
        if x >= 0:
            continue
        else:
            total += x
            x_max = max(x_max, x)

    if total != 0:
        print(total)
        print(x_max)
    else:
        print('NO')

#some_review_002()

##===================================================================##
def some_review_003():
    '''
    На обработку поступает последовательность из 7 целых чисел.
    Известно, что вводимые числа по абсолютной величине не превышают 10^6.
    Нужно написать программу, которая выводит на экран сумму всех чётных чисел последовательности или 0,
    если таковых нет.
    '''
    s = 0
    for _ in range(7):
        n = int(input())
        if n % 2 == 0:
            s += n
    print(s)

#some_review_003()

##===================================================================##
def some_review_004():
    '''
    На обработку поступает натуральное число.
    Известно, что вводимые числа по абсолютной величине не превышают 10^6.
    Нужно написать программу, которая выводит на экран максимальную цифру числа кратную 3.
    Если таковых нет, вывести "NO".
    '''
    n = int(input())
    max_digit = -1

    while n > 0:
        digit = n % 10
        if digit % 3 == 0:
            if max_digit < digit:
                max_digit = digit
        n //= 10

    if max_digit == -1:
        print('NO')
    else:
        print(max_digit)

#some_review_004()

##===================================================================##
def nested_cicles_001():
    n = int(input())

    for _ in range(n):
        for _ in range(3):
            print(n, end=' ')
        print()

#nested_cicles_001()

##===================================================================##
def nested_cicles_002():
    n = int(input())

    for i in range(n):
        for _ in range(5):
            print(i + 1, end=' ')
        print()

#nested_cicles_002()

##===================================================================##
def sum_table():
    n = int(input())

    for i in range(1, n + 1):
        for j in range(1, 10):
            print(i, '+', j, '=', i + j)
        print()

#sum_table()

##===================================================================##
def print_triangle():
    n = int(input())

    for i in range(0, (n + 1) // 2):
        for _ in range(i + 1):
            print('*', end='')
        print()
    for i in range((n + 1) // 2, n):
        for _ in range(n - i, 0, -1):
            print('*', end='')
        print()

#print_triangle()

##===================================================================##
def digital_triangle():
    n = int(input())

    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end='')
        print()

#digital_triangle()

##===================================================================##
def nested_cicles_003():
    '''
    Нахождение корней уравнения перебором
    '''
    total = 0
    for n in range(1, 11):
        for k in range(1, 11):
            for m in range(1, 10):
                if 28 * n + 30 * k + 31 * m == 365:
                    total += 1
                    print('n =', n, 'k =', k, 'm =', m)
    print('Общее количество натуральных решений =', total)

#nested_cicles_003()

##===================================================================##
# b + k + t = 100
# 10b + 5k + 0.5t <= 100
'''
В 1769 году Леонард Эйлер сформулировал обобщенную версию Великой теоремы Ферма, предполагая, что по крайней мере nn энных степеней необходимо для получения суммы, которая сама является энной степенью для n > 2n>2.
Напишите программу для опровержения гипотезы Эйлера (продержавшейся до 1967 года), и найдите четыре положительных целых числа, сумма 5-х степеней которых равна 5-й степени другого положительного целого числа.

Таким образом, найдите пять натуральных чисел a, b, c, d, e удовлетворяющих условию: a^5+b^5+c^5+d^5=e^5.

В ответе укажите сумму a+b+c+d+ea+b+c+d+e.

Примечание 1. Используйте вложенный цикл for.
Примечание 2. Считайте, что числа a, b, c, d, ea,b,c,d,e не превосходят 150150.
Примечание 3. Программа может работать дольше чем обычно. В зависимости от способа решения задачи на выполнение программы может уходить до нескольких минут. Попробуйте сократить количество вложенных циклов. 
'''
'''
flag = 0
for a in range(1, 150):
    for b in range(1, 150):
        for c in range(1, 150):
            for d in range(1, 150):
                for e in range(1, 150):
                    if pow(a, 5) + pow(b, 5) + pow(c, 5) + pow(d, 5) == pow(e, 5):
                        print(a + b + c + d + e)
                        flag = -1
                        break
                if flag == -1:
                    break
            if flag == -1:
                break
        if flag == -1:
            break
    if flag == -1:
        break
'''

##===================================================================##
def print_number_triangle_001():
    n = int(input())
    k = 1

    for i in range(n):
        for _ in range(i + 1):
            print(k, end=' ')
            k += 1
        print()

#print_number_triangle()

##===================================================================##
def print_number_triangle_002():
    n = int(input())

    for i in range(1, n + 1):
        k = 2
        for j in range(1, 2 * i):
            if j <= i:
                print(j, end='')
            elif j > i:
                print(j - k, end='')
                k += 2
        print()

#print_number_triangle_002()

##===================================================================##
'''
def max_sum_of_deviders():
    a, b = int(input()), int(input())
    total_max = a + 1
    num_extremum = a

    for j in range(a, b + 1):
        total = j + 1
        x = j
        for i in range(2, j // 2 + 1):
            while x % i == 0:
                total += i
                x //= i
        if total_max < total:
            total_max = total
            num_extremum = j

    print(num_extremum, total_max)
'''
def max_sum_of_deviders():
    a, b = int(input()), int(input())
    total_max = a + 1
    num_extremum = a

    for j in range(a, b + 1):
        total = 0
        for i in range(1, j + 1):
            if j % i == 0:
                total += i
        if total_max <= total:
            total_max = total
            num_extremum = j

    print(num_extremum, total_max)

#max_sum_of_deviders()

##===================================================================##
def graph_of_num_of_deviders():
    n = int(input())

    for i in range(1, n + 1):
        print(i, end='')
        #counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                print('+', end='')
        print()

#graph_of_num_of_deviders()

##===================================================================##
def digital_root():
    n = int(input())

    while n > 9:
        n = (n // 10) + (n % 10)

    print(n)

#digital_root()

##===================================================================##
def sum_of_factorials():
    n = int(input())
    total = 0

    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        total += fact

    print(total)

#sum_of_factorials()

##===================================================================##
def all_primes_in_range():
    a, b = int(input()), int(input())

    for i in range(a, b + 1):
        prime = 'YES'
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                prime = "NO"
                break
        if prime == 'NO' or i == 1:
            continue
        else:
            print(i)


#all_primes_in_range()

##===================================================================##
'''n = 8
count = 0
maximum = -(pow(10, 6))
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')'''

##===================================================================##
'''n = 4
count = 0
maximum = -(pow(10, 6))
for _ in range(1, n + 1):
    x = int(input())
    if x % 2 == 1:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')'''

##===================================================================##
'''n = int(input())

count3 = 0
for c in str(n):
    if int(c) == 3:
        count3 += 1

last_digit = n % 10
count_last_dig = 0
for c in str(n):
    if c == str(last_digit):
        count_last_dig += 1

count_even = 0
for c in str(n):
    if int(c) % 2 == 0:
        count_even += 1

total5 = 0
for c in str(n):
    if int(c) > 5:
        total5 += int(c)

production7 = 1
for c in str(n):
    if int(c) > 7:
        production7 *= int(c)

count05 = 0
for c in str(n):
    if int(c) == 0 or int(c) == 5:
        count05 += 1

print(count3)
print(count_last_dig)
print(count_even)
print(total5)
print(production7)
print(count05)'''

##===================================================================##
def ramanudjan_numbers():
    n = 11
    counter = 0
    flag = 0
    k = 20

    #while counter <= 4:
    for _ in range(1, n):
        for a in range(1, k * n + 1):
            for b in range(1, k * n + 1):
                for c in range(1, k * n + 1):
                    for d in range(1, k * n + 1):
                        if a == b or c == d or a == c or a == d:
                            continue
                        elif (pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3)) and (pow(a, 3) + pow(b, 3)) < 32832:
                            print(a, '* 3', '+', b, '* 3', '=', c, '* 3', '+', d, '* 3', '=', pow(a, 3) + pow(b, 3))
                            counter += 1
                            if counter == 40:
                                flag = -1
                                break
                    if flag == -1:
                        break
                if flag == -1:
                    break
            if flag == -1:
                break
        if flag == -1:
            break

#ramanudjan_numbers()

##===================================================================##
def count_of_near_repeat():
    s = input()
    counter = 0
    old_char = s[0]

    for i in range(len(s)):
        if i == 0:
            continue
        if s[i] == old_char:
            counter += 1
        old_char = s[i]

    print(counter)

#count_of_near_repeat()

##===================================================================##
def type_of_letters():
    s = input()
    count_a = count_b = 0

    for c in s:
        if c.lower() in 'аеёиоуыэюя':
            count_a += 1
        elif c.lower() in 'бвгджзйклмнпрстфхцчшщ':
            count_b += 1

    print('Количество гласных букв равно', count_a)
    print('Количество согласных букв равно', count_b)

#type_of_letters()

##===================================================================##
def decimal_to_binary():
    n = int(input())
    bin_str = bin_rev = ''

    while n != 0:
        bin_rev += str(n % 2)
        n //= 2

    for i in range(len(bin_rev) - 1, -1, -1):
        bin_str += bin_rev[i]

    print(bin_str)

#decimal_to_binary()

##===================================================================##
def frequency_counter():
    s = input()
    freq_max = s[0]
    freq_count = 0

    for c in s:
        if s.count(c) >= freq_count:
            print('Before:', 'freq_count =', freq_count, '|', 'freq_max =', freq_max)
            freq_max = c
            freq_count = s.count(c)
            print('After:', 'freq_count =', freq_count, '|', 'freq_max =', freq_max) 

    print(freq_max)

#frequency_counter()

##===================================================================##
def second_found():
    s = input()

    if s.count('f') == 1:
        print(-1)
    elif s.count('f') == 0:
        print(-2)
    else:
        print(s.find('f') + s[s.find('f') + 1:].find('f') + 1)

#second_found()

##===================================================================##
def rotate_substring():
    s = input()

    print(s[:s.find('h') + 1] + s[s.find('h') + 1:s.rfind('h')][::-1] + s[s.rfind('h'):])

#rotate_substring()

##===================================================================##
def remove_over_step(): # плохое решение %). Можно в цикле проверять индексы на делимость на 3 и выводить те что не делятся с end=''
    s = input()
    s_cut = ''
    i = 0

    while i < len(s) - 2:
        s_cut += s[i + 1:i + 3]
        i += 3

    s_cut += s[i + 1:]
    print(s_cut)

#remove_over_step()

##===================================================================##
def cubes_generator():
    n = int(input())
    cubes = []

    for _ in range(n):
        cubes.append(int(input()) ** 3)

    print(cubes)

#cubes_generator()

##===================================================================##
def generator_of_list_001():
    start = ord('a')
    total_list = []

    for i in range(26):
        total_list.append(chr(start + i) * (i + 1))

    print(total_list)

#generator_of_list_001()

##===================================================================##
def list_of_deviders():
    n = int(input())
    deviders = []

    for i in range(1, n + 1):
        if n % i == 0:
            deviders.append(i)

    print(deviders)

#list_of_deviders()

##===================================================================##
def sums_of_nearest():
    n = int(input())
    n_list = []
    sums = []

    for _ in range(n):
        n_list.append(int(input()))

    for i in range(1, len(n_list)):
        sums.append(n_list[i] + n_list[i - 1])

    print(sums)

#sums_of_nearest()

##===================================================================##
def remove_even_indexes():
    n = int(input())
    n_list = []

    for _ in range(n):
        n_list.append(int(input()))

    del n_list[1::2]
    print(n_list)

#remove_even_indexes()

##===================================================================##
def print_char_from_strings():
    n = int(input())
    n_list = []

    for _ in range(n):
        n_list.append(input())

    k = int(input())

    for el in n_list:
        if len(el) < k:
            continue
        else:
            print(el[k - 1], end='')

#print_char_from_strings()

##===================================================================##
def prind_all_char():
    n = int(input())
    n_list = []

    for _ in range(n):
        n_list.extend(input())

    print(n_list)

#prind_all_char()

##===================================================================##
def  lists_test_001():
    n = int(input())
    n_list = []

    for _ in range(n):
        n_list.append(int(input()))

    print(*n_list, sep='\n')
    print()

    for el in n_list:
        print(el ** 2 + 2 * el + 1)

#lists_test_001()

##===================================================================##
def lists_test_002():
    n = int(input())
    n_list = []

    for _ in range(n):
        n_list.append(int(input()))

    max_el = max(n_list)
    min_el = min(n_list)
    for i in range(len(n_list)):
        if n_list[i] == max_el:
            del n_list[i]
            break
    for i in range(len(n_list)):
        if n_list[i] == min_el:
            del n_list[i]
            break

    print(*n_list, sep='\n')

#lists_test_002()

##===================================================================##
def return_uniq():
    n = int(input())
    n_list = []

    for _ in range(n):
        el = input()
        if el not in n_list:
            n_list.append(el)

    print(*n_list, sep='\n')

#return_uniq()

##===================================================================##
def return_strings_by_substring(): # google search #1
    n = int(input())
    n_list = []
    for _ in range(n):
        n_list.append(input())
    s_req = input()

    for el in n_list:
        if s_req.lower() in el.lower():
            print(el)

#return_strings_by_substring()

##===================================================================##
def return_strings_by_substring_002(): # google search #2
    n = int(input())
    n_list = []
    for _ in range(n):
        n_list.append(input())
    k = int(input())
    k_list = []
    for _ in range(k):
        k_list.append(input())

    for el in n_list:
        count = 0
        for req in k_list:
            if req.lower() in el.lower():
                count += 1
                if count == k:
                    print(el)

#return_strings_by_substring_002()

##===================================================================##
def sort_by_sign():
    n = int(input())
    n_list = []
    for _ in range(n):
        n_list.append(int(input()))
    minuses = []
    zeros = []
    pluses = []

    for el in n_list:
        if el < 0:
            minuses.append(el)
        elif el == 0:
            zeros.append(el)
        else:
            pluses.append(el)

    print(*minuses + zeros + pluses, sep='\n')

#sort_by_sign()

##===================================================================##
def how_many_pairs():
    s_list = input().split()
    count = 0

    for el in s_list:
        if s_list.count(el) > 1:
            count += (s_list.count(el) * (s_list.count(el) - 1) // 2) / s_list.count(el)

    print(int(count))

#how_many_pairs()

##===================================================================##
def min_max_exchange():
    s_list = input().split()
    n_list = []
    for el in s_list:
        n_list.append(int(el))
    max_index = n_list.index(max(n_list))
    min_index = n_list.index(min(n_list))
    minimal, maximal = min(n_list), max(n_list)
    n_list[max_index] = minimal
    n_list[min_index] = maximal

    print(*n_list)

#min_max_exchange()

##===================================================================##
def find_articles():
    s_list = input().lower().split()
    art_count = 0

    for el in ['a', 'an', 'the']:
        art_count += s_list.count(el)

    print('Общее количество артиклей:', art_count)

#find_articles()

##===================================================================##
def clear_comments():
    n = int(input()[1:])
    code = []
    for _ in range(n):
        code.append(input())

    for el in code:
        if '#' in el:
            print(el[:el.find('#')].rstrip())
        else:
            print(el.rstrip())

#clear_comments()

##===================================================================##
def sort_by_select():
    a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
    #a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72]
    n = len(a)

    for i in range(n - 1):
        maxi = n - i - 1
        for j in range(n - i - 1):
            if a[j] > a[maxi]:
                maxi = j
        if maxi != n - i - 1:
            a[n - i - 1], a[maxi] = a[maxi], a[n - i - 1]

    print(a)

#sort_by_select()

##===================================================================##
def is_correct_phone():
    s = input()
    is_phone = 'NO'

    if s.count('-') == 2 or s.count('-') == 3:
        s_list = s.split('-')
        if len(s) == 12 and len(s_list) == 3 and len(s_list[0]) == len(s_list[1]) == 3 and len(s_list[2]) == 4:
            for el in s_list:
                if el.isdigit(): 
                    is_phone = 'YES'
                else:
                    is_phone = 'NO'
                    break
        elif len(s) == 14 and len(s_list) == 4 and s_list[0] == '7' and len(s_list[1]) == len(s_list[2]) == 3 and len(s_list[3]) == 4:
            for el in s_list:
                if el.isdigit(): 
                    is_phone = 'YES'
                else:
                    is_phone = 'NO'
                    break

    print(is_phone)

#is_correct_phone()

##===================================================================##
def draw_triangle_001():
    for i in range(1, 11):
        print('*' * i)

#draw_triangle_001()  # вызов функции

##===================================================================##
def convert_to_miles(km):
    return km * 0.6214

# считываем данные
#num = int(input())

# вызываем функцию
#print(convert_to_miles(1))
#print(convert_to_miles(5))
#print(convert_to_miles(10))

##===================================================================##
def find_all(target, symbol):
    inserts = []
    shift = 0
    while target.find(symbol) != -1:
        inserts.append(target.find(symbol) + shift)
        shift += target.find(symbol) + 1
        target = target[target.find(symbol) + 1:]
    return inserts

# считываем данные
#s = input()
#char = input()

# вызываем функцию
#print(find_all(s, char))
#print(find_all('abcdabcaaaba', 'a'))
#print(find_all('abcadbcaaa', 'e'))
#print(find_all('abcadbcaaad', 'd'))

##===================================================================##
def merge(list1, list2):
    return sorted(list1 + list2)

# считываем данные
#numbers1 = [int(c) for c in input().split()]
#numbers2 = [int(c) for c in input().split()]

# вызываем функцию
#print(merge(numbers1, numbers2))
#print(merge([1, 2, 3], [5, 6, 7, 8]))
#print(merge([1, 7, 10, 16], [5, 6, 13, 20]))

##===================================================================##
def quick_merge(list1, list2):
    '''
    1. Создаем численные указатели p1 = 0 и p2 = 0 на начала обоих списков list1 и list2 соответственно;
    2. На каждом шаге берем меньший из двух элементов list[p1] и list2[p2];
    3. Записываем его в результирующий список; 
    4. Увеличиваем указатель на первый элемент списка (p1 или p2) из которого был взят элемент на 11;
    5. Когда один из начальных списков закончился, добавляем все оставшиеся элементы второго списка в результирующий список.
    '''
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    
    return result

##===================================================================##
def merge_digit_strings(n, n_list):
    n_list = [[int(j) for j in el] for el in n_list]
    total_list = []
    for i in range(n):
        total_list = quick_merge(total_list, n_list[i])

    return total_list

#merge_digit_strings()

#n = int(input())
#n_list = [input().split() for _ in range(n)]

#print(*merge_digit_strings(n, n_list))

##===================================================================##
def is_valid_triangle(side1, side2, side3):
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        return True
    else:
        return False

'''
short version^
def is_valid_triangle(side1, side2, side3):
    return side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2
'''
# считываем данные
#a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
#print(is_valid_triangle(a, b, c))

##===================================================================##
def is_prime(num):
    
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

# считываем данные
#n = int(input())

# вызываем функцию
#print(is_prime(n))

##===================================================================##
def get_next_prime(num):
    next_prime = num + 1
    while is_prime(next_prime) is False:
        next_prime += 1
    
    return next_prime

# считываем данные
#n = int(input())

# вызываем функцию
#print(get_next_prime(n))

##===================================================================##
def is_password_good(password):
    if len(password) < 8 or password.islower() or password.isupper() or password.isdigit() or password.isalpha():
        return False
    for el in list(password):
        if el.isdigit():
            break
    else:
        return False
    
    return True
    

# считываем данные
#txt = input()

# вызываем функцию
#print(is_password_good(txt))

##===================================================================##
def is_one_away(word1, word2):
    counter = 0

    if len(word1) != len(word2):
        return False
    
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            counter += 1
    if counter != 1:
        return False

    return True

# считываем данные
#txt1 = input()
#txt2 = input()

# вызываем функцию
#print(is_one_away(txt1, txt2))
#print(is_one_away('bike', 'hike'))
#print(is_one_away('water', 'wafer'))
#print(is_one_away('abcd', 'abpo'))
#print(is_one_away('abcd', 'abcde'))

##===================================================================##
def is_palindrome(text):
    text = [el.lower() for el in text if el.isalpha()]
    return text == text[::-1]

# считываем данные
#txt = input()

# вызываем функцию
#print(is_palindrome(txt))
#print(is_palindrome('А роза упала на лапу Азора.'))
#print(is_palindrome('Gabler Ruby - burrel bag!'))
#print(is_palindrome('BEEGEEK'))

##===================================================================##
def is_num_palindrome(num):
    return num.isdigit() and str(num) == str(num)[::-1]

def is_num_prime(num):

    if not num.isdigit or int(num) < 2:
        return False
    else:
        for i in range(2, int(num)):
            if int(num) % i == 0:
                return False
    
    return True

def is_num_even(num):
    return num.isdigit() and int(num) % 2 == 0
    
def is_valid_password(password):
    if password.count(':') == 2 and len(password.split(':')) == 3:
        pass_list = password.split(':')
        return is_num_palindrome(pass_list[0]) and is_num_prime(pass_list[1]) and is_num_even(pass_list[2])
    else:
        return False

# считываем данные
#psw = input()

# вызываем функцию
#print(is_valid_password(psw))
#print(is_valid_password('1221:101:22'))
#print(is_valid_password('565:30:50'))
#print(is_valid_password('112:7:9'))
#print(is_valid_password('1221:101:22:22'))

##===================================================================##
def is_correct_bracket(text):
    text = [el for el in text if el in ['(', ')']]
    
    if text.count('(') == text.count(')'):
        for _ in range(text.count(')')):
            mark = text.index(')')
            if text[mark - 1] == '(' and mark - 1 >= 0:
                text.pop(mark)
                text.pop(mark - 1)
            else:
                return False
    else:
        return False
    
    return True

# считываем данные
#txt = input()

# вызываем функцию
#print(is_correct_bracket(txt))
#print(is_correct_bracket('()(()())'))
#print(is_correct_bracket(')(())('))

##===================================================================##
def convert_to_python_case(text):
    py_text = text[0].lower()
    
    for c in text[1:]:
        if c.isupper():
            py_text += '_' + c.lower()
        else:
            py_text += c

    return py_text

# считываем данные
#txt = input()

# вызываем функцию
#print(convert_to_python_case(txt))
#print(convert_to_python_case('ThisIsCamelCased'))
#print(convert_to_python_case('IsPrimeNumber'))

##===================================================================##
from math import pi

def get_circle(radius):
    return 2 * pi * radius, pi * radius ** 2

# считываем данные
#r = float(input())

# вызываем функцию
#length, square = get_circle(r)
#print(length, square)

##===================================================================##
from math import sqrt

def solve(a, b, c):
    disc = b ** 2 - 4 * a * c

    if disc == 0:
        return -(b / (2 * a))
    else:
        x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return min(x1, x2), max(x1, x2)

# считываем данные
#a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
#x1, x2 = solve(a, b, c)
#print(x1, x2)
#print(solve(1, -4, -5))
#print(solve(-2, 7, -5))
#print(solve(1, 2, 1))

##===================================================================##
def draw_triangle():
    #h = 15
    w = 8
    for i in range(1, w + 1):
        print(' ' * (w - i) + '*' * (i * 2 - 1))

# основная программа
#draw_triangle()

##===================================================================##
def get_shipping_cost(quantity):
    firts = 1000
    step = 120
    return firts + (quantity - 1) * step

# считываем данные
#n = int(input())

# вызываем функцию
#print(get_shipping_cost(n))
#print(get_shipping_cost(1))
#print(get_shipping_cost(3))

##===================================================================##
def factorial(num):
    prod = 1
    for i in range(1, num + 1):
        prod *= i
    return prod

def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# считываем данные
#n = int(input())
#k = int(input())

# вызываем функцию
#print(compute_binom(n, k))
#print(compute_binom(2, 5))

##===================================================================##
def number_to_words(num): # 1 <= num <= 99
    num_10 = num // 10
    num_01 = num % 10
    low = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    mids = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    high = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

    if num < 10:
        return low[num - 1]
    elif 10 <= num < 20:
        return mids[num_01]
    elif num % 10 == 0:
        return high[num_10 - 2]
    else:
        return high[num_10 - 2] + ' ' + low[num_01 - 1]

# считываем данные
#n = int(input())

# вызываем функцию
#print(number_to_words(n))
#print(number_to_words(9))
#print(number_to_words(11))
#print(number_to_words(29))
#print(number_to_words(20))
#print(number_to_words(99))

##===================================================================##
def get_month(language, number):
    ru_m = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    en_m = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    if language == 'ru':
        return ru_m[number - 1]
    else:
        return en_m[number - 1]

# считываем данные
#lan = input()
#num = int(input())

# вызываем функцию
#print(get_month(lan, num))
#print(get_month('ru', 1))
#print(get_month('ru', 12))
#print(get_month('en', 1))
#print(get_month('en', 10))

##===================================================================##
def is_magic(date):
    date = date.split('.')
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    
    if day * month == year % 100:
        return True

    return False

# считываем данные
#date = input()

# вызываем функцию
#print(is_magic(date))
#print(is_magic('10.06.1960'))
#print(is_magic('11.06.1960'))

##===================================================================##
def is_pangram(text):
    text_list = sorted(set(c.lower() for c in text if c.isalpha()))
    alfa_list = [chr(i) for i in range(97, 123)]

    return sorted(text_list) == alfa_list

# считываем данные
#text = input()

# вызываем функцию
#print(is_pangram(text))
#print(is_pangram('Jackdaws love my big sphinx of quartz'))
#print(is_pangram('The jay pig fox zebra and my wolves quack'))
#print(is_pangram('Hello world'))

##===================================================================##
def cesar_algorithm_encoder():
    '''
    Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям и использует шифр Цезаря.
    Это их и подвело, ведь данный шифр очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира, поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения.
    Напишите программу для декодирования этого шифра.

    Формат входных данных:
    - В первой строке дается число n (1 <= n <= 25) – сдвиг
    - во второй строке даётся закодированное сообщение в виде строки со строчными латинскими буквами.
    '''
    shift = int(input())
    encoded = input()
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded = ''

    for c in encoded:
        decoded += alfabet[alfabet.find(c) - shift]

    print(decoded)

#cesar_algorithm_encoder()

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