import random

matrix = [[random.randint(1,10) for i in range(4)]for i in range(4)]
print(f'转置之前的矩阵为{matrix}')
matrix_T = list(zip(*matrix))
print(f'转置之后的矩阵为{matrix_T}')
