# 随机生成一个 10 以内整数平方的列表，要求从大到小排序。
import random

lst = [(random.randint(1,10))**2 for i in range(10)]
lst.sort(reverse=True)
print(lst)