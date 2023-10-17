import re

f = open("config.txt")
lines = f.read()
f.close()
lst = lines.split("\n")
s = open("new_config.txt", "w")
for i in range(len(lst)):
    lst1 = re.findall("[^:]{1,}", lst[i])
    if i == 0:
        s.write("<" + lst1[0] + ">" + lst1[1] + "</" + lst1[0] + ">")
    else:
        s.write("\n" + "<" + lst1[0] + ">" + lst1[1] + "</" + lst1[0] + ">")
