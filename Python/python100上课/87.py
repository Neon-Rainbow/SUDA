a = input('输入一个字符串')
b = int(input(f'选 1 英文字符全部转换为大写，选 2 小写英文字符全部转换为大写'))
if b == 1:
    print(a.upper())
elif b == 2:
    print(a.lower())
else:
    print('wrong input')
