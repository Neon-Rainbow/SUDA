# 给定字符串，将其中的单词倒序输出。例：给定"What a wonderful day!"，输出："day!
# wonderful a What"。
import re

a = input('请输入字符串')
word = re.compile('[A-Za-z]+')
lst = re.findall(word, a)
lst.reverse()
for i in lst:
    print(i,end=' ')