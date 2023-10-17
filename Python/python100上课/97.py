a = 'google.com'
dic = {}
for i in a:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i]+=1
print(dic)