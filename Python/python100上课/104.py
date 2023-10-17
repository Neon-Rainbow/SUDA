import re


def hui_wen_chuan():
    a = input('输入字符串')
    b = re.compile(',| \. | \? |!|\s')
    clear_a = re.sub(b, '', a)
    if clear_a == clear_a[::-1]:
        return True
    else:
        return False



print(hui_wen_chuan())
