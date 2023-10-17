import os

c = r"Folder"
lst = os.listdir(c)
f = open(os.path.join(c, "merge.txt"), "w")
for i in lst:
    s = open(os.path.join(c, i))
    lines = s.read()
    f.write(lines + "\n")
f.close()
