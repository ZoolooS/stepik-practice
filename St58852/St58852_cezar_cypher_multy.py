def cezar(mode, lang, shift):
    '''
    Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.

    Она должна запрашивать у пользователя следующие данные:
    - направление: шифрование или дешифрование;
    - язык алфавита: русский или английский;
    - шаг сдвига (со сдвигом вправо).

    Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).
    Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.
    Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".
    '''
    # ====== imports block ================================== #


    # ====== defining functions ============================= #
    def validate_mode(s):
        if s.upper() == 'E' or s.upper() == 'З':
            return 'encode'
        elif s.upper() == 'D' or s.upper() == 'Р':
            return 'decode'
        else:
            print('Вы ввели некорректное значение. Попробуйте снова.')
            validate_mode(input('(E / D) >> '))


    def validate_lang(s):
        if s.upper() == 'E' or s.upper() == 'А':
            return 'en'
        elif s.upper() == 'R' or s.upper() == 'Р':
            return 'ru'
        else:
            print('Вы ввели некорректное значение. Попробуйте снова.')
            validate_mode(input('(E / R) >> '))


    def validate_int(s):
        if s.isdigit():
            return int(s)
        else:
            print('Вы ввели некорректное значение. Попробуйте снова.')
            validate_int(input('(Целое число) >> '))


    def cezar_encode(decoded, lang, shift):

        if lang == 'en':
            alfabet = ''.join([chr(i) for i in range(97, 123)])  # 'abcdefghijklmnopqrstuvwxyz' # Номера Юникода для латиницы: A-Z - 65-90, a-z - 97-122
            print('alfabet =', alfabet)
        elif lang == 'ru':
            alfabet = ''.join([chr(i) for i in range(1072, 1104)])  # Номера Юникода для русских букв: А-Я - 1040-1071 + Ё-1025, а-я - 1072-1103 + ё-1105
            print('alfabet =', alfabet)
        encoded = ''

        for c in decoded:
            if c.lower() in alfabet:
                if c.isupper():
                    encoded += (alfabet[(alfabet.find(c.lower()) + shift) % len(alfabet)]).upper()
                elif c.islower():
                    encoded += alfabet[(alfabet.find(c) + shift) % len(alfabet)]
            else:
                encoded += c
        
        return encoded


    def cezar_decode(encoded, lang, shift):
        
        if lang == 'en':
            alfabet = ''.join([chr(i) for i in range(97, 123)])  # 'abcdefghijklmnopqrstuvwxyz' # Номера Юникода для латиницы: A-Z - 65-90, a-z - 97-122
        elif lang == 'ru':
            alfabet = ''.join([chr(i) for i in range(1072, 1104)])  # Номера Юникода для русских букв: А-Я - 1040-1071 + Ё-1025, а-я - 1072-1103 + ё-1105
        decoded = ''
        
        for c in encoded:
            if c.lower() in alfabet:
                if c.isupper():
                    decoded += (alfabet[(alfabet.find(c.lower()) - shift) % len(alfabet)]).upper()
                elif c.islower():
                    decoded += alfabet[(alfabet.find(c) - shift) % len(alfabet)]
            else:
                decoded += c

        return decoded

    # ====== main code ====================================== #
    #print('>>> Шифратор/дешифратор для шифра Цезаря <<<\n---')

    #mode = validate_mode(input('Будем зашифровывать (E / З) или расшифровывать (D / Р)? >> '))
    #lang = validate_lang(input('На каком языке текст? ([E]nglish / [А]нглийский или [R]ussian / [Р]усский])? >> '))
    #shift = validate_int(input('С каким сдвигом будем шифровать/дешифровать? >> '))

    #if mode == 'encode':
    #    result = cezar_encode(input('Введите строку для шифрования:\n>> '), lang, shift)
    #elif mode == 'decode':
    result = cezar_decode('Hawnj pk swhg xabkna ukq nqj.', lang, shift)
    #else:
    #    print('Что-то пошло не так..')

    print(result)

    # ====== end of code ==================================== #

print('====================')
for i in range(1, 26):
    cezar('E', 'en', i)
print('====================')