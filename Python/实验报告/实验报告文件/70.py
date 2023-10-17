lst = (65.5, 70.2, 100.5, 45.5, 88.8, 55.5, 73.5, 67.8)

sum = sum(lst)
avg = sum/len(lst)
def var(b):
    a = 0
    for i in range(len(b)):
        a += (int(i)-avg)**2
    return a/len(b)


print(var(lst))
