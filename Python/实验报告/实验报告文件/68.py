n = int(input('输入矩阵的行数'))
m = int(input('输入矩阵的列数'))
A = [[0 for i in range(m)] for i in range(n)]
B = [[0 for i in range(m)] for i in range(n)]
C = [[0 for i in range(m)] for i in range(n)]
D = [[0 for i in range(m)] for i in range(n)]
for i in range(0, n):
    for j in range(0, m):
        A[i][j] = int(input(f'Please input A[{i},{j}]'))
for i in range(0, n):
    for j in range(0, m):
        B[i][j] = int(input(f'Please input B[{i},{j}]'))
        C[i][j] = A[i][j] + B[i][j]
print(C)
