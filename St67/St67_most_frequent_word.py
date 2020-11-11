'''
Приложение читает текстовый файл и выводит наиболее часто встречающееся слово и количество его повторений.
Примечание:
  * Наличие пунктуации в исходнике допустимо, но подсчёт будет вестись не корректно, словом считается текст между пробельными символами.
  * Регистр слов/букв не учитывается специально.
  * Если слов с максимальным повторением несколько, то выводится "наименьшее" в лексикографическом смысле.
'''
def most_frequent_word():
    import os

    path = os.path.join('.', 'St67_most_frequent_word_input.txt')
    with open(path, 'r') as inf:
        s_list = []
        [s_list.extend(el) for el in [line.lower().strip().split() for line in inf]]

    s_dict = {}
    [s_dict.update({el: s_list.count(el)}) for el in set(s_list)]

    #max(s_dict.values())
    print(min([el for el in s_dict.keys() if s_dict[el] == max(s_dict.values())]), max(s_dict.values()))
    
    #with open('St67_most_frequent_word_output.txt', 'w') as ouf:
    #    ouf.write(s_out)

most_frequent_word()