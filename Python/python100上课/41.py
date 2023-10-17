import random

dire = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
name = input('输入账户名')
password = input('输入密码')
if name in dire.keys():
    if dire[name] == password:
        yanzhenma = random.randint(1000,9999)
        print(yanzhenma)
        a = int(input('请输入验证码'))
        if a == yanzhenma:
            print('成功登陆')
        else:
            print('验证码错误')
    else:
        print('账号或密码错误')
else:
    print('账号或密码错误')
