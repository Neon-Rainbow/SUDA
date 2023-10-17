f = open("students_data.txt")
lines = f.readlines()
f.close()
lst = []
for i in lines:
    if i[:-1] == "\n":
        lst.append(i[:len(i) - 1].split(" "))
    else:
        lst.append(i.split(" "))
s = open("students_5.txt", "w")
for i in lst:
    if int(i[2]) > 3:
        s.write(i[0] + " " + i[1] + "\n")
s.close()
