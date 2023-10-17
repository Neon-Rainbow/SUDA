f=open("word.txt")
lines=f.read()
f.close()
lst=lines.split("\n")
s=open("new_word.txt","w")
a=0
for i in lst:
    if i[0] in ["a","e","i","o","u"]:
        if a==0:
            a=1
        else:
            s.write("\n")
        s.write(i)