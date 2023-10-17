# IPv4 采用 32 位 2 进制位数记录地址，在实际使用中 IPv4 地址通常使用点分十进制记
# 法表示，即使用.将 IP 地址平分为 4 段，每段地址使用 0~255 范围内的十进制无符号整
# 数表示，例如 192.168.1.1。另外 IPv4 地址根据第一段 IP 的值分为 5 类地址，如下表所
# 示，例如 192.168.1.1 是一个 C 类地址。编写一个程序，从键盘输入一个字符串形式的
# IP 地址，判断 IP 地址是否是合法的 IPv4 地址，如果是合法地址，判断其地址类型。
# 类型 第一段地址范围
# A 类 0~127
# B 类 128~191
# C 类 192~223
# D 类 224~239，组播地址
# E 类 240~254，保留为研究测试使用
import re

address = input('请输入一个IP地址')
standard_address = re.compile('[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}')
lst = re.findall('[0-9]{1,}', address)
if re.match(standard_address, address):
    IP = int(lst[0])
    if 0 <= IP <= 127:
        print("A类")
    elif 128 <= IP <= 191:
        print('B类')
    elif 192 <= IP <= 223:
        print("C")
    elif 224 <= IP <= 239:
        print("D")
    elif 240 <= IP <= 254:
        print('测试地址')
    else:
        print('非法地址')
else:
    print('非法地址')
