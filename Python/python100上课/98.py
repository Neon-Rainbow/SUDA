import re

a = input("待过滤字符串")
b = input("过滤字符集合")
lst = []
c = ""
for i in b:
    lst.append(i)
for i in a:
    if i not in lst:
        c += i
print(c)