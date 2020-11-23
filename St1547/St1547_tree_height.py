'''
Программа счтает высоту дерева.

На вход подаётся натуральное число n, а затем ряд целых чисел parent(0), parent(n-1).
Для каждого 0 <= i <= n-1, parent(i) - родитель вершины i
Если parent(i) = -1, то i является корнем.

Гарантруется, что корень ровно один.
Гарантируется, что последовательность задаёт дерево.

Ограничения 1 <= n <= 10^5.
'''
# ====== imports block ================================== #


# ====== function declaration =========================== #
'''
def chopper(tree):  # def chopper(tree, chop=1):
    cuted_tree = tree
    cuted_tree = {k: v for k, v in cuted_tree.items() if v != []}  # Чистим от элементов с пустыми значениями
#    chop += 1
#    print(f'cuted_tree on step {chop} before remove = {cuted_tree}')
#    print('cuted_tree.keys() = ', *cuted_tree.keys())
#    print('cuted_tree.values() = ', *cuted_tree.values())

    [[v.remove(el) for el in v[:] if str(el) not in cuted_tree.keys()] for v in cuted_tree.values()]
#    print(f'cuted_tree on step {chop} after remove = {cuted_tree}')

    return cuted_tree
'''


def chopper(tree):  # def chopper(tree, chop=1):
    tree = {k: v for k, v in tree.items() if v != []}  # Чистим от элементов с пустыми значениями
#    chop += 1
#    print(f'cuted_tree on step {chop} before remove = {cuted_tree}')
#    print('cuted_tree.keys() = ', *cuted_tree.keys())
#    print('cuted_tree.values() = ', *cuted_tree.values())

    [[v.remove(el) for el in v[:] if str(el) not in tree.keys()] for v in tree.values()]
#    print(f'cuted_tree on step {chop} after remove = {cuted_tree}')

    return tree


def cut_branch(tree):
    cuted_tree = tree
    cuts = []
    for i in range(n):
        if str(i) not in parents:
#            cuted_tree.pop(i)
            cuted_tree[i] = ''
#            print('cuted_tree_clear = ', cuted_tree)
        else:
#            cuted_tree.append(parents[i])
#            print('cuted_tree_pass = ', cuted_tree)
#            cuted_tree.pop(i)
            cuted_tree[i] = parents[i]
    print('cuted_tree = ', cuted_tree)
    print('cuts = ', cuts)

    return cuted_tree, cuts


# ====== main code ====================================== #
n = int(input())
cuts = tree = parents = input().split()
print('parents = ', parents)
count = 0
for i in range(n):
    count += 1
    tree, cuts = cut_branch(tree)
    print('tree = ', tree)
    print('cuts_out = ', cuts)

print(count)

'''
tree = {str(i): [] for i in range(-1, n)}
#print('tree_start = ', tree)
[[tree[str(parents[i])].append(i)] for i in range(n)]
#print('tree_end = ', tree)

#tree_height = chopper(tree)
#print('tree_height_out = ', tree_height)

tree_height = 0
while len(tree) > 1:
    tree = chopper(tree)
    tree_height += 1
#    print('tree_height = ', tree_height)
#    print(tree)

print(tree_height)
'''
# ====== end of code ==================================== #
