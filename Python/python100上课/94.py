def f94():
    s = str(input('请输入一个字符串'))
    if len(s) < 2:
        return ''
    else:
        return s[0:2:1] + s[-2:]


print(f94())
