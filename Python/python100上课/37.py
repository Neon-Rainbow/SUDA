a = int(input('输入0到100的整数'))
if a<0 or a>100:
    print('不在范围内')
else:
    if a%3 == 0:
        print(f"{a}能被三整除")
    else:
        print(f"{a}不能被3整除")