# 自行定义两个列表，列表元素个数大于 10。将 2 个列表合并，然后截取第 8 至第 15 个
# 元素，输出最后得到的结果。
import random

lst1 = [random.randint(1,10) for i in range(11)]
lst2 = [random.randint(1,10) for i in range(11)]
lst = lst1 + lst2
print(lst[8:16])