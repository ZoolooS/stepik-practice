'''
Приложение читает ссылку из сопроводительного файла.
Затем последовательно открывает, читает и возвращает ссылки из остальных файлов пока не найдёт файл с первым словом 'We'.
Содержимое этого файла нужно вернуть в качестве решения.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
'''
# ====== imports block ================================== #
import requests, os, io

# ====== function declaration =========================== #
def get_first_url():
    path = os.path.join('.', 'St67_recurrent_file_reading_input.txt')
    with io.open(path, 'r', encoding='utf-8') as inf:
        return inf.readline().strip()  # first url


def get_content_from_url(url):
    return requests.get(url).text.strip()  # s_out


def print_to_file(s_out):
    #print('s_out =', type(s_out))
    print('s_out ============\n' + s_out + '\n===================')
    with open('St67_recurrent_file_reading_output.txt', 'w') as ouf:
        ouf.write(s_out)


def main():
    base = 'https://stepic.org/media/attachments/course67/3.6.3/'
    url = get_first_url()
    s_out = get_content_from_url(url)

    while s_out.split()[0] != 'We':
        with open('St67_recurrent_file_reading_link_list.txt', 'a') as ouf:
            ouf.write(base + s_out + '\n')
        s_out = get_content_from_url(base + s_out)

    if s_out.split()[0] == 'We':
        #print('We? ==>', s_out.split()[0])
        #print('s_out ============\n' + s_out + '\n===================')
        #print('s_out is', type(s_out))
        print_to_file(s_out)
    else:
        print('Что-то пошло не так..')


# ====== main code ====================================== #
main()

# ====== end of code ==================================== #