def verify_brackets():
    '''
    Программа проверяет соглассованность скобок.
    Если есть несогласование, то выводит позицию первой ошибки или первой скобки которая не имеет закрывающей пары.
    Если скобки соглассованы, то выводит 'Success'
    ([](){([])}) - Success
    ()[]} - 5
    ({[](){([])})
    {{[()]] - 7
    '''
    s = input()
    br = [['(', ')', 0], ['[', ']', 0], ['{', '}', 0]]
    unpaired = []
    stop = False

    for i in range(len(s)):
        if (s[i] not in [el[0] for el in br]) and (s[i] not in [el[1] for el in br]):
            continue

        for el in br:
            if s[i] == el[0]:
                el[2] += 1
                unpaired.append([el[0], i])
                print('unpaired_upp = ', unpaired)
        
        for el in br:
            if s[i] == el[1]:
                el[2] -= 1
                try:
                    popped = unpaired.pop()
                    print('unpaired_pop = ', unpaired)
                    if popped[0] != el[0]:
                        print('popped = ', i + 1)
                        stop = True
                        break
                except IndexError:
                    print('unp_try_pop = ', i + 1)
                    stop = True
                    break
        if stop == True:
            break

    if br[0][2] == br[1][2] == br[2][2] == 0:
        print('Success')
    elif unpaired != [] and stop == False:
        print('unpaired = ', unpaired)
        print('unp_not_empty', unpaired[0][1] + 1)
       
verify_brackets()