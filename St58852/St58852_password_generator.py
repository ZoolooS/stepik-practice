'''
Описание проекта:
программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, 
а также на то, какие символы требуется в него включить, а какие исключить.
'''
# ====== imports block ================================== #
from random import choice, shuffle

# ====== defining functions ============================= #
def validate_yn_answers(s):
    if s.upper() == 'Y' or s.upper() == 'Д':
        return True
    elif s.upper() == 'N' or s.upper() == 'Н':
        return False
    else:
        print('Вы ввели некорректное значение. Попробуйте снова.')
        validate_yn_answers(input('(Y / N) >> '))


def validate_int(s):
    if s.isdigit():
        return int(s)
    else:
        print('Вы ввели некорректное значение. Попробуйте снова.')
        validate_int(input('(Целое число) >> '))


def take_dict_settings():
    use_digits = validate_yn_answers(input('Использовать цифры (0123456789)? (Y / N) >> '))
    use_uppercase = validate_yn_answers(input('Использовать прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? (Y / N) >> '))
    use_lowercase = validate_yn_answers(input('Использовать строчные буквы (abcdefghijklmnopqrstuvwxyz)? (Y / N) >> '))
    use_punctuation = validate_yn_answers(input('Использовать символы (!#$%&*+-=?@^_)? (Y / N) >> '))
    use_exclude = validate_yn_answers(input('Исключать символы с похожим написанием (il1Lo0O)? (Y / N) >> '))

    return use_digits, use_uppercase, use_lowercase, use_punctuation, use_exclude


def generate_dict(use_digits, use_uppercase, use_lowercase, use_punctuation, use_exclude):
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    exclude = 'il1Lo0O'
    chars = []

    if use_digits:
        chars.extend(digits)
    if use_uppercase:
        chars.extend(uppercase_letters)
    if use_lowercase:
        chars.extend(lowercase_letters)
    if use_punctuation:
        chars.extend(punctuation)
    if use_exclude:
        chars = [c for c in chars if c not in exclude]

    return chars


def generate_password(length, chars):
    shuffle(chars)
    return [choice(chars) for el in range(length)]

# ====== main code ====================================== #
print('>>> Генератор паролей <<<\n---')

n_pass = validate_int(input('Сколько паролей вам нужно? >> '))
l_pass = validate_int(input('Желаемая длина паролей? >> '))
chars = generate_dict(*take_dict_settings())

print('====================')
for _ in range(n_pass):
    print(*generate_password(l_pass, chars), sep='')
print('====================')

# ====== end of code ==================================== #