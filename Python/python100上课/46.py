N = int(input('小明带的钱数为'))
n = int(N / 15)
lst = []
for a in range(n):
    for b in range(n):
        for c in range(n):
            if 3 * a + 5 * b + c == n:
                lst.append(4 * a + 7 * b + c)
print(max(lst))
