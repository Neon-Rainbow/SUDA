dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'a': 2, 'b': 3, 'c': 1}
lst = []
for i in dic1.keys():
    if i in dic2.keys():
        lst.append(i)
print(lst)