'''

'''
# ====== imports block ================================== #


# ====== function declaration =========================== #
def s_c_cutter_alt(s):
    char = s[0]
    for el in s:
        if el != char:
            if s.index(el) == 1:
                print(f'{char} ==> {s[1:]}')
                return char, s[1:]
            else:
                print(f'{str(s.index(el)) + char} ==> {s[s.index(el):]}')
                return str(s.index(el)) + char, s[s.index(el):]


def s_c_cutter(s):
    char = s[0]
#    if len(s) == 1:
#        return char, []
    for i in range(len(s)):
        if i == len(s) - 1:
            return char, []
        elif s[i] != char:
            if i == 1:
#                print(f'{char} ==> {s[i:]}')
                return char, s[i:]
            else:
#                print(f'{str(i) + char} ==> {s[i:]}')
                return str(i) + char, s[i:]


def simple_compression():
    s = input()
    s_cut = s[:]
    result = ''

    while s_cut:
        part, s_cut = s_c_cutter(s_cut)
        result += part

    print(result)


def simple_compression_alt():
    s = input()
    result = ''
    count = 1

    if len(s) == 1:
        result = s

    for i in range(1, len(s)):
        if s[i] == s[i - 1] and i == len(s) - 1:
            result += str(count + 1) + s[i - 1]
        if s[i] == s[i - 1]:
            count += 1
        elif s[i] != s[i - 1] and i == len(s) - 1:
            if count == 1:
                result += s[i - 1] + s[i]
            else:
                result += str(count) + s[i - 1] + s[i]
        else:
            if count == 1:
                result += s[i - 1]
            else:
                result += str(count) + s[i - 1]
                count = 1

    print(result)

# ====== main code ====================================== #
# simple_compression()
simple_compression_alt()

# ====== end of code ==================================== #
