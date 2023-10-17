dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'a': 2, 'b': 3, 'c': 1}
lst = []
for i in dic1.keys():
    for j in dic2.keys():
        if dic1[i] == dic2[j]:
            lst.append((i,j))
print(lst)