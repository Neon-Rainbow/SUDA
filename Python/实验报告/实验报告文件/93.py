lst = [0 for i in range(10)]
for i in range(10):
    lst[i] = input(f'第{i + 1}个字母为')
lst1 = sorted(lst, reverse=True)
print(lst1)
lst2 = sorted(lst, reverse=False)
print(lst2)