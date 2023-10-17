lst = ['alpha', 'all', 'dig', 'date', 'egg']
lst2 = {}
for item in lst:
    count = []
    if item[0] not in lst2.keys():
        count = [item]
        lst2[item[0]] = count
    else:
        count = [i for i in lst2[item[0]]]+[item]
        lst2[item[0]] = count
print(lst2)