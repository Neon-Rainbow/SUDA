n = int(input('n = '))
for i in range(n + 1):
    if i == 0:
        print(' ', end=' ')
    else:
        if i != n:
            print(i, end=' ')
        else:
            print(i)
for i in range(1, n + 1):
    print(i, end=' ')
    for j in range(1, i + 1):
        if i != j:
            print(i * j, end=' ')
        else:
            print(i * j)
