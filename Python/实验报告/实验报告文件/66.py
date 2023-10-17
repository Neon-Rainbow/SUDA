n = int(input('Please input the number of numbers: '))
if n != 0:
    lst = [0 for i in range(n)]
    for i in range(n):
        lst[i] = int(input(f'Please input number {i + 1}:'))
    print(f'sum = {sum(lst)}')
else:
    print('退出程序')
