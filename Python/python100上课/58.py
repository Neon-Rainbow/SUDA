a = int(input(f'输入一个整数'))
for i in range(a):
    star = str('*'*(2*i+1))
    print(star.center(2*a))