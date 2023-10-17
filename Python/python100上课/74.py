b = input('输入大写英文字母')
a = b.upper()
dire = {}


def zidian():
    for i in a:
        count = 1
        if i not in dire.keys():
            dire[i] = count
        else:
            count = dire[i]+1
            dire[i] = count
    return dire


print(zidian())
