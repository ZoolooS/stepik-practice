'''
Приложение читает текстовый файл со статистикой оценок абитуриентов и выводит средние значения оценок для каждого абитуриента.
Примечание:
  * range(1, 4) в итераторе по предметам (при подсчёте среднего по каждому предмету) можно заменить на автоподсчёт длины "строки", но мне было лень %)
'''
def average_grade():
    import os, io

    path = os.path.join('.', 'St67_average_grade_input.txt')
    with io.open(path, 'r', encoding='utf-8') as inf:
        grade_list = []
        grade_list = [line.strip().split(';') for line in inf]
    
    avg_by_name = [sum([int(grade) for grade in el[1:]]) / len(el[1:]) for el in grade_list]
    avg_by_lesson = [(sum([int(el[i]) for el in grade_list]) / len(grade_list)) for i in range(1, 4)]

    s_out = ''
    s_out = '\n'.join([str(el) for el in avg_by_name]) + '\n' + ' '.join([str(el) for el in avg_by_lesson])

    #print(grade_list)
    #print(*avg_by_name, sep='\n')
    #print(*avg_by_lesson)
    #print('=============')
    #print(s_out)

    with open('St67_average_grade_output.txt', 'w') as ouf:
        ouf.write(s_out)

average_grade()