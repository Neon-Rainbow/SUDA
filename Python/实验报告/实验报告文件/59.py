star1 = str('* ')
star2 = str('*')
n = int(input('请输入正六边形边的长度='))
for i in range(-n+1,n):
    i = abs(i)
    num = 2*n-2-i
    line = star1*num+star2
    print(line.center(4*n))