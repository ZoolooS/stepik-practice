"""Программа эмулирует работу с пространствами имен.
https://stepik.org/lesson/24460/step/10?unit=6766

Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:
  - create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
  - add <namespace> <var> – добавить в пространство <namespace> переменную <var>
  - get <namespace> <var> – получить имя пространства, из которого будет взята
        переменная <var> при запросе из пространства <namespace>,
        или None, если такого пространства не существует

Формат входных данных:
    В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
    В каждой из следующих n строк дано по одному запросу.
    Запросы выполняются в порядке, в котором они даны во входных данных.
    Имена пространства имен и имена переменных представляют из себя строки длины не более 10,
        состоящие из строчных латинских букв.

Формат выходных данных:
    Для каждого запроса get выведите в отдельной строке его результат.
"""
# ====== imports block ================================== #


# ====== function declaration =========================== #
def get_actual_namespace(namespace, var):
    if var in namespace[2]:
        return namespace[0]

    return None


def slide_through_branch(namespace, var):
    actual_namespace = get_actual_namespace(namespace, var)
    if namespace[1]:
        for nmsp in namespace[1]:
            tmp = slide_through_branch(nmsp, var)
            return tmp if tmp else actual_namespace
    else:
        return actual_namespace


def path_to_namespace_by_name(cur_nmsp, name, path=''):
    if cur_nmsp[0] == name:
        return f'[{path}]' + '[1]' if path else '[1]'
    elif not cur_nmsp[1]:
        print('Error: Unknown parent namespace')
        return None

    print(f'{cur_nmsp[1] = }')
    for idx, nmsp in enumerate(cur_nmsp[1]):
        print(f'{nmsp = } | {name = } | {idx = }')
        path = path_to_namespace_by_name(nmsp, name, f'{idx}')
        path = path if path else None

    return path


# ====== main code ====================================== #
n = int(input())
# cmd, nsp, arg = input().split()
cmds = [input().split() for _ in range(n)]
print(cmds)
glb = ['global', [['foo', [], []], ['xxx', [], []]], []]
print(f'{glb = }')
print(f'{glb[1] = }')
print('===========================')

for cmd in cmds:
    if cmd[0] == 'create':
        print(f'{cmd[2] = }')
        exe = 'glb' + f'{path_to_namespace_by_name(glb, cmd[2])}'
        # eval(exe) = [cmd[1], [], [], []]
        print(f'{exe = }')
        print('> End command\n')

    elif cmd[0] == 'add':
        ...

    elif cmd[0] == 'get':
        ...

# nmsps = ['global', [['foo', [], ['b'], []]], ['a'], ['foo']]
# nmsps = ['global', [], ['a'], []]
# nmsps = ['global',
#          [['foo',
#            [['bar',
#              [['zzz',
#                [],
#                ['k']]],
#              ['a']]],
#            ['c']]],
#          ['a']]
# print(slide_through_branch(glb, 'a'))
# print(slide_through_branch(glb, 'c'))

# nmsps = ['global', [], [], []]  # ['namespace', [[chld_nmsps]], [vars], [list_of_branch_nmsps]]
# # add global a
# nmsps = ['global', [], ['a'], []]
# # create foo global
# nmsps = ['global', [['foo', [], [], []]], ['a'], ['foo']]
# # add foo b
# nmsps = ['global', [['foo', [], ['b'], []]], ['a'], ['foo']]
# # get foo a
# slide_through_branch(nmsps, 'a')
# # get foo c
# slide_through_branch(nmsps, 'c')

# glbl = ['global_nms']
# print('global_start = ', glbl)
# for cmd in cmds:
#     if cmd[0] == 'add':
#         if cmd[1] in glbl:
#             pass
#         else:
#             glbl.append(cmd[2])
#     elif cmd[0] == 'create':
#         if cmd[1] in glbl:
#             pass
#         else:
#             glbl.append([f'{cmd[2]}_nms', f'{cmd[1]}_nms'])
#     elif cmd[0] == 'get':
#         pass
# print('global_end = ', glbl)


# Делаем List'ы для global с его непосредственным содержимым
# и для каждого вложенного namespace'а
# По сути нужно сделать дерево с ветками-list'ами

# ====== end of code ==================================== #
