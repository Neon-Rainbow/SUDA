import re


def username_check():
    username = input('请输入用户名')
    if (re.match('[0-9]', username) and re.search('!|\?|@|:', username) is None) and (len(username) >= 6 is True):
        if len(username) >= 6:
            print('输入正确')
            password_check()
        else:
            print('test2')
            username_check()
    else:
        print('test1')
        print(re.match('[0-9]', username),'test',re.search('!|\?|@|:', username))

def password_check():
    password = input('请输入密码')
    if re.search('[0-9]', password) and re.search('[a-z]', password) and re.search('[A-Z]', password) is not None:
        if len(password) >= 6:
            print('密码输入错误')
            return password_check()
        else:
            return password_adain_check()


def password_adain_check():
    password_again = input('请再次输入密码')
    if password_again == password_check::password:
        print('注册成功')
    else:
        return password_adain_check()


print(username_check())