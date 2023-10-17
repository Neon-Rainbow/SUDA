count = 0
for a in range(1, 200):
    for b in range(1, 200):
        for c in range(1, 200):
            if 15 * a + 3 * b + 2 * c == 200:
                count += 1
print(count)
