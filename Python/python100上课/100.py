import re

URL = 'http://192.168.1.1:8080/index.html?a=1'
a = re.compile('://|/|\?')
lst1 = re.split(a, URL)
lst2 = ['协议', '主机域名或 IP', '端口', '路径', '参数']
for i,j in zip(lst2,lst1):
    print(f'{i}:{j}')