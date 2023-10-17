import re

f = open("article.txt")
lines = f.read()
f.close()
lst = re.findall("[a-zA-Z]{1,}", lines)
D = {}
for i in lst:
    if len(i) not in D:
        D[len(i)] = [i]
    else:
        D[len(i)].append(i)
lst1 = sorted(D)
s = open("new_article_classify.txt", "w")
a = 0
for i in lst1:
    if a == 0:
        a = 1
    else:
        s.write("\n")
    s.write(str(i) + ":" + str(len(D[i])) + "," + " ".join(D[i]))
s.close()
