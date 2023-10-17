f = open("students_data.txt")
lines = f.read()
f.close()
print(lines)
lst = lines.split("\n")
for i in lst:
    lst1 = i.split(" ")
    print(lst1)
    print("{0:<10s}{1:<15s}{2:>5s}".format(lst1[0], lst1[1], lst1[2]))
for i in range(len(lst)):
    lst[i] = lst[i].split(" ")
lst.sort(key=lambda temp: int(temp[0]))
s1 = input()
f = open("students_data.txt", "w")
a = 0
for i in lst:
    if s1 <= i[0]:
        if a == 0:
            a = 1
            f.write(" ".join(i))
        else:
            f.write("\n" + " ".join(i))
f.close()
