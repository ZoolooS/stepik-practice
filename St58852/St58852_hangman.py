'''
Игра "Виселица"
Описание проекта: программа загадывает слово, а пользователь должен его угадать.
Изначально все буквы слова неизвестны. Также рисуется виселица с петлей.
Пользователь предлагает букву, которая может входить в это слово.
Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове.
Если такой буквы нет, к виселице добавляется круг в петле, изображающий голову.
Пользователь продолжает отгадывать буквы до тех пор, пока не отгадает всё слово.
За каждую неудачную попытку добавляется еще одна часть туловища висельника (обычно их 6: голова, туловище, 2 руки и 2 ноги.
'''
# ====== imports block ================================== #
from random import choice

# ====== defining functions ============================= #
def get_riddle_word():
    dictpath = 'c:/_zooloos/_dev/Stepik/St58852/dict.txt'
    f = open(dictpath, 'r', encoding="utf-8")
    riddle = choice(f.readlines())[:-1]
    if riddle.isalpha():
        f.close()
        return riddle.upper()
    else:
        get_riddle_word()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        ''',
        # голова, торс, обе руки, одна нога
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
            -
        ''',
        # голова, торс, обе руки
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |      
            -
        ''',
        # голова, торс и одна рука
        '''
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
            -
        ''',
        # голова и торс
        '''
            --------
            |      |
            |      O
            |      |
            |      |
            |     
            -
        ''',
        # голова
        '''
            --------
            |      |
            |      O
            |    
            |      
            |     
            -
        ''',
        # начальное состояние
        '''
            --------
            |      |
            |      
            |    
            |      
            |     
            -
        '''
    ]

    return stages[tries]


def validate_guess(guess):
    if guess.isalpha() and len(guess) == 1:
        return guess, 'char'
    elif guess.isalpha() and len(guess) > 1:
        return guess, 'word'
    else:
        print('Вы ввели какое-то непотребство. попробуйте снова')
        validate_guess(input('Слово или буква. >> ').upper())


def gameplay(riddle):
    word_completion = '-' * len(riddle)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    print('>>> Поиграй со мной в угадайку! Успеешь? <<<\n---')
    print('Я загадал слово (кириллицей), а у тебя есть 6 неправильных попыток')
    print(display_hangman(6))
    print('>>', word_completion)

    guess, g_type = validate_guess(input('Попытай удачу - назови слово или букву. >> ').upper())

    if g_type is 'word' and guess in guessed_words:
        pass
    elif g_type is 'char' and guess in guessed_letters:
        pass



# ====== main code ====================================== #
gameplay(get_riddle_word())

# ====== end of code ==================================== #