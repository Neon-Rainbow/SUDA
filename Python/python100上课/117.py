f = open("filenames.txt")
lines = f.read()
f.close()
lst = lines.split("\n")
lst.insert(0, lst[-1])
for i in range(1, len(lst)):
    s = open(lst[i], "w")
    s.write(lst[i - 1])
    s.close()
