'''
Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число.
Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.
Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.

Оптимальный алгоритм угадывания: положим left = 1 и right = 100.
 - Называем число, равное middle = (left + right) // 2;
 - Если число middle равно задуманному число, то мы угадали!;
 - Если число middle меньше задуманного числа, то положим left = middle + 1 и продолжим алгоритм;
 - Если число middle больше задуманного числа, то положим right = middle - 1 и продолжим алгоритм.
'''
# ====== imports block ================================== #
from random import randint

# ====== defining functions ============================= #
def min_guess_count(num):
    from math import ceil, log

    return ceil(log(int(num), 2))


def is_data_valid(s, limit):
    return s.isdigit() and 1 <= int(s) <= limit


def repeat_game():
    repeat = input('Хотите сыграть ещё? Y / N: ').upper()
    if repeat == 'Y':
        return True
    elif repeat == 'N':
        return False
    else:
        print('Вы ввели что-то непотребное. Попробуйте снова')
        repeat_game()


def choose_mode():
    mode = input('Хотите угадывать от 1 до 100 или можете указать верхний предел (Y / число): ')
    if str(mode).upper() == 'Y':
        return 100
    elif mode.isdigit():
        return int(mode)
    else:
        print('Вы ввели что-то непотребное. Попробуйте снова...')
        choose_mode()


def guess_random_num(num = 100):  # main algorithm
    rand = randint(1, int(num))
    count = 0
    print(f'Я загадал. Угадайте число от 1 до {num}.')

    while True:
        guess = input('Ваша догадка: ')
        count += 1

        if is_data_valid(guess, num):
            guess = int(guess)
        else:
            print(f'А может быть все-таки введёте целое число от 1 до {num}?')
            count = 0
            continue
        
        if guess == rand:
            print('Вы угадали, поздравляю!')
            print(f'Вам потребовалось {count} попыток при гарантированном минимуме в {min_guess_count(num)} попыток.\n--')
            if repeat_game():
                guess_random_num(choose_mode())
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break
        elif guess > rand:
            print('Слишком много, попробуйте еще раз...')
            continue
        else:
            print('Слишком мало, попробуйте еще раз...')
            continue


# ====== main code ====================================== #
print('<<<  Добро пожаловать в числовую угадайку  >>>\n--')
guess_random_num(choose_mode())

# ====== end of code ==================================== #