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
#def bubo_read_and_return_file(rel_path='.', strip='no', split=('no')):  # Вставить из библиотеки


def return_first_url():
    path = os.path.join('.', 'St67_recurrent_file_reading_input.txt')
    #with io.open(path, 'r', encoding='utf-8') as inf:
    with open(path, 'r') as inf:
        return inf.readline().strip()  # first url


def recurrence_by_url(url):
    base = 'https://stepic.org/media/attachments/course67/3.6.3/'
    r = requests.get(url).text.strip()

    if r.split()[0] != 'We':
        with open('St67_recurrent_file_reading_link_list.txt', 'a') as ouf:
            ouf.write(base + r + '\n')
        recurrence_by_url(base + r)
    
    if r.split()[0] == 'We':
        print('We? ==>', r.split()[0])
        print('r.text ============\n' + r + '\n===================')
        print('r.text =', type(r))

    return r  # s_out


def print_to_file(s_out):
    print('s_out =', type(s_out))
    print('s_out ============\n' + s_out + '\n===================')

    with open('St67_recurrent_file_reading_output.txt', 'w') as ouf:
        ouf.write(s_out)


# ====== main code ====================================== #
print_to_file(recurrence_by_url(return_first_url()))

# ====== end of code ==================================== #