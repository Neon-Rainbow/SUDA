import random

a = random.randint(0, 100)
b = int(input('猜数字，输入一个数'))
while True:
    if b > a:
        print('大了')
        b = int(input('重新输入'))
    elif b < a:
        print('小了')
        b = int(input('重新输入'))
    else:
        print("恭喜，猜正确了")
        break
