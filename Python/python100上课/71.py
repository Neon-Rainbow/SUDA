tup = (1, 2, 2, 3, 4, 5)
lst = []
for i in tup:
    if i not in lst:
        lst.append(i)
print(lst)