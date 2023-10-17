import random

lst1 = ['Fang','Peng',"Wu",'Sun','Zhao',"Wu"]
lst2 = ['Haonan',"Guang","Xiaolong","Liulei","Zichu",'Jiajun']
dire = {}
for i in zip(lst2,lst1):
    dire[i] = random.randint(18,100)
print(dire)