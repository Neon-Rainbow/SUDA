# 101. 英语语法中,动词的第三人称单数形式规则简要概括(不完全)如下:
# A)     如果动词以 y 字母结尾,则去掉 y 并加上ids。
#
# a)    如果动词以 o , bh , s , sh , x , z 字母结尾,则加上 ds。
# b)     默认直接在动词最后加上字母 s。
# 请编写一个程序,对于任意给定的一个动词,返回其第三人称单数形式。
a = input("输入一个动词")
if a.endswith("y"):
    b = a[:-1] + 'ies'
elif a.endswith("o") or a.endswith("ch") or a.endswith("s") or a.endswith("sh") or a.endswith("x") or a.endswith("x"):
    b = a + 'es'
else:
    b = a + 's'
print(b)