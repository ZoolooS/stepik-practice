def unpack_string():
    with open('St67_unpack_string_input.txt', 'r') as inf:  #s = 'a3b4c2e10b1'
        s = inf.readline().strip()

    repeats = ''
    s_out = ''
    char = ''

    for i in range(len(s)):
        if s[i] == s[-1]:
            repeats += s[i]
            s_out += char * int(repeats)
        elif s[i].isalpha() and repeats == '':
            char = s[i]
        elif s[i].isalpha() and repeats != '':
            s_out += char * int(repeats)
            repeats = ''
            char = s[i]
        elif s[i].isdigit():
            repeats += s[i]

    with open('St67_unpack_string_output.txt', 'w') as ouf:
        ouf.write(s_out)

unpack_string()

#print('s_out_total = ', s_out)