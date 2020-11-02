# ====== defining functions ============================= #
def cezar_encode(decoded, lang, shift):

    alfabet = ''.join([chr(i) for i in range(97, 123)])
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


# ====== main code ====================================== #
s = input()
s_word = ''
flag = 0
result = ''

for c in s:
    if c.isalpha():
        s_word += c
        flag = 1
    elif flag == 0:
        result += c
    else:
        result += cezar_encode(s_word, 'en', len(s_word)) + c
        s_word = ''
        count = 0

print(result)

# ====== end of code ==================================== #