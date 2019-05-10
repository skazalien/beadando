ls1 = []
# n1 = 10
# n2 = 10
n1 = int(input("n1: "))
n2 = int(input("n2: "))

ls1 = []
for i in range(n1):
    ls2 = []
    for j in range(n2):
        ls2.append(0)
    ls1.append(ls2)

for i in range(n1):
    ls2 = []
    for j in range(0, min(i, n2)):
        if j == 0 or j == i:
            ls1[i][j] = 1
        else:
            ls1[i][j] = ls1[i - 1][j - 1] + ls1[i - 1][j]

for k in ls1:
    print(' ' * 2 * n1, end='')
    n1 -= 1
    for l in k:
        if l > 0:
            print('{:>4}'.format(l), end='')
    print()
