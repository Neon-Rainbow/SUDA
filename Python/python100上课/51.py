a = int(input('输入一个十进制整数'))
b = ''
test_count = 0
while a >= 2:
    test_count += 1
    c = str(a%2)
    a = a//2
    b += c
if a == 1:
    b += str(1)
print(b[::-1])
