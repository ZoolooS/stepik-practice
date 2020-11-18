'''
Программа счтает высоту дерева.

На вход подаётся натуральное число n, а затем ряд целых чисел parent(0), parent(n-1).
Для каждого 0 <= i <= n-1, parent(i) - родитель вершины i
Если parent(i) = -1, то i является корнем.

Гарантруется, что корень ровно один.
Гарантируется, что последовательность задаёт дерево.

Ограничения 1 <= n <= 10^5.


5
4 -1 4 1 1
Выход: 3

5
-1 0 4 0 3
Выход: 4

10
9 7 5 5 2 9 9 9 2 -1
Sample Output: 4
'''
# ====== imports block ================================== #


# ====== function declaration =========================== #


# ====== main code ====================================== #
n = int(input())
#verts = [i for i in range(n)]
parents = input().split()

print('parents = ', parents)
tree = {str(i): [] for i in range(-1, n)}
print('tree_start = ', tree)
[[tree[str(parents[i])].append(i)] for i in range(n)]
print('tree_end = ', tree)



#print(tree_height)
# ====== end of code ==================================== #