print(f'请选择你最喜欢的编程语言\n[1]Python\n[2]C++\n[3]Java\n[4]退出')
a = int(input('输入编号'))
b = f'是一款非常优秀的编程语言'
if a == 1:
    print(f'Python{b}')
elif a == 2:
    print(f'C++{b}')
elif a == 3:
    print(f'Java{b}')
elif a == 4:
    print('退出成果')
else:
    print('输出有误')