'''
Приложение читает ссылку из сопроводительного файла.
Затем последовательно открывает, читает и возвращает ссылки из остальных файлов пока не найдёт файл с первым словом 'We'.
Содержимое этого файла нужно вернуть в качестве решения.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
'''
# ====== imports block ================================== #
import requests, os, io

# ====== defining functions ============================= #
def recurrence_by_url(url):
    base = 'https://stepic.org/media/attachments/course67/3.6.3/'
    r = requests.get(url)
    if r.text.strip().split()[0] == 'We':
        return r.text.strip()
    else:
        recurrence_by_url(base + r.text.strip())


def recurrent_file_reading():
    path = os.path.join('.', 'St67_recurrent_file_reading_input.txt')
    with io.open(path, 'r', encoding='utf-8') as inf:
        url = inf.readline().strip()

    s_out = str(recurrence_by_url(url))

    with open('St67_recurrent_file_reading_output.txt', 'w') as ouf:
        ouf.write(s_out)


# ====== main code ====================================== #
recurrent_file_reading()

# ====== end of code ==================================== #