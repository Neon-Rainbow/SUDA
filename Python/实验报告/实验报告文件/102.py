import re


def judge_password():
    a = input('请输入密码')
    if len(a) < 8 and re.search('[0,9]+', a) is None  and re.search('[a-z]+', a) is None and re.search('[A-Z]+', a) is None:
        return False
    else:
        return True


print(judge_password())
