def prime(n):
    lst = []
    for i in range(2, n):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
                lst.append(i)
    return lst
print(prime(100000))