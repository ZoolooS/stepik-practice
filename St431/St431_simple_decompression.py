'''

'''
# ====== imports block ================================== #


# ====== function declaration =========================== #
def spliter(compressed: str):
    splitted = []
    before = ''
    for i in range(len(compressed)):
        if compressed[i].isdigit() and before == 'digit':
            splitted[-1][0] += compressed[i]
        elif compressed[i].isdigit():
            splitted.append([compressed[i]])
            before = 'digit'
        elif compressed[i].isalpha() and before == 'digit':
            splitted[-1].append(compressed[i])
            before = ''
        else:
            splitted.append(['1', compressed[i]])

    return splitted


def decompressor(c_parts):
    return [int(el[0]) * el[1] for el in c_parts]


def spliter_gen(compressed: str):
    k = ''
    for i in range(len(compressed)):
        if compressed[i].isalpha() and k == '':
            yield ('1', compressed[i])
        elif compressed[i].isalpha():
            yield (k, compressed[i])
            k = ''
        elif compressed[i].isdigit():
            k += compressed[i]


def decompressor_gen(c_parts):
    return [int(k) * ch for k, ch in c_parts]


def printer(d_parts: list):
    print(*d_parts, sep='')


def main():
    compressed = input()

#    c_parts = spliter(compressed)
#    print(c_parts)
#    c_parts = spliter_gen(compressed)
#    print('c_parts =', c_parts)
#    print('c_parts_unpack =', list(c_parts))
#    d_parts = decompressor(c_parts)
#    d_parts = decompressor_gen(c_parts)
#    d_parts = decompressor_gen(spliter_gen(compressed))
#    print('d_parts =', d_parts)
    printer(decompressor_gen(spliter_gen(compressed)))


# ====== main code ====================================== #
main()

# ====== end of code ==================================== #
