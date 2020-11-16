'''
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Программа читает этот файл и подсчитывает для каждого класса средний рост учащегося.

Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост

Класс обозначается только числом. Буквенные модификаторы не используются.
Номер класса может быть от 1 до 11 включительно.
В фамилии нет пробелов, а в качестве роста используется натуральное число,
но при подсчёте среднего требуется вычислить значение в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый).
Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.

В качестве ответа прикрепите файл с полученными данными о среднем росте.
'''
# ====== imports block ================================== #
import os, io

# ====== function declaration =========================== #


# ====== main code ====================================== #
path = os.path.join('.', 'St67_average_height_by_class_input.txt')
with io.open(path, 'r', encoding='utf-8') as inf:
    height_list = [line.strip().split('\t') for line in inf]

h_count = [[str(i), 0] for i in range(1, 12)]
av_h_dict = [[str(i), 0] for i in range(1, 12)]

[[h_count[i - 1].insert(1, h_count[i - 1].pop(1) + 1) for i in range(1, 12) if el[0] == str(i)] for el in height_list]
[[av_h_dict[i - 1].insert(1, av_h_dict[i - 1].pop(1) + int(el[2])) for i in range(1, 12) if el[0] == str(i)] for el in height_list]

out_list = [[str(i), 0] for i in range(1, 12)]
[[out_list[i].insert(1, (out_list[i].pop(1) + av_h_dict[i][1]) / h_count[i][1])] if h_count[i][1] != 0 else [out_list[i].insert(1, '-')] for i in range(11)]

s_out = '\n'.join([f'{el[0]} {el[1]}' for el in out_list])
print(f's_out =\n{s_out}')

with open('St67_average_height_by_class_output.txt', 'w') as ouf:
    ouf.write(s_out)
# ====== end of code ==================================== #