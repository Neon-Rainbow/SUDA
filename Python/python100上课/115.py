f = open("Numbers.txt")
lines = f.read()
f.close()
lst = lines.split("\n")
lst.sort(key=lambda temp: float(temp))
s = open("Sort.txt", "w")
for i in lst:
    s.write(i + "\n")
sum = 0
for i in lst:
    sum += float(i)
a = sum / len(lst)
b = 0
for i in lst:
    b += (float(i) - a) ** 2
b = b / len(lst)
s.write(str(sum) + "\n" + str(b))
s.close()
