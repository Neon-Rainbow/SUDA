import re

f = open("article.txt")
lines = f.read()
f.close()
lst = re.findall("[^.,?!;]+", lines)
lst1 = re.findall("[.,?!;]+", lines)
s = open("new_article.txt", "w")
for i in range(len(lst)):
    lst2 = lst[i].split(" ")
    lst2[0] = lst2[0].upper()
    s.write(" ".join(lst2) + lst1[i] + "\n")
s.close()
