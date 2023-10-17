def zhao_ge_shu():
    sum = 0
    for a in range(7):
        for b in range(7):
            for c in range(7):
                for d in range(7):
                    for e in range(7):
                        for f in range(7):
                            for g in range(7):
                                answer = int(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g))
                                if answer % 2 == 1:
                                    sum += 1
    return sum


print(zhao_ge_shu())
