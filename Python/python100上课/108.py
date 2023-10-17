import re

username = input('请输入用户名')
if re.match('\d', username) and re.search('!|\?|@|:', username) is None:
    password = input('请输入密码')
    if re.search('[0-9]', password) and re.search('[a-z]', password) and re.search('[A-Z]', password) is not None:
        if len(password) >= 6:
            password_again = input('请再次输入密码')
            if password_again == password:
                print('注册成功')
        else:
            print('密码格式错误')
    else:
        ''
else:
    print('用户名格式错误')