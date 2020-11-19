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
def chopper(tree, chop=1):
    cuted_tree = tree
    cuted_tree = {k: v for k, v in cuted_tree.items() if v != []}
    chop += 1
    print(f'cuted_tree on step {chop} before remove = {cuted_tree}')
    print('cuted_tree.keys() = ', *cuted_tree.keys())
    print('cuted_tree.values() = ', *cuted_tree.values())
#    [[v.remove(v) for el in v if v not in cuted_tree.keys()] for v in cuted_tree.values()]
    for v in cuted_tree.values():
#       tmp = []
        for el in v:
            if str(el) in cuted_tree.keys():
                print('boo')
#                tmp.append(el)
                v.remove(el)
#        cuted_tree[k] = tmp
    print(f'cuted_tree on step {chop} after remove = {cuted_tree}')

#    return chopper(cuted_tree, chop)

#    return chop


# ====== main code ====================================== #
n = int(input())
# verts = [i for i in range(n)]
parents = input().split()

print('parents = ', parents)
tree = {str(i): [] for i in range(-1, n)}
print('tree_start = ', tree)
[[tree[str(parents[i])].append(i)] for i in range(n)]
print('tree_end = ', tree)

tree_height = chopper(tree)
print('tree_height_out = ', tree_height)


# print(tree_height)
# ====== end of code ==================================== #
