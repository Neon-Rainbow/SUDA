import random

a = random.randint(1, 9)
b = a
n = int(input('n = '))
sum = a
gong_shi = f"{a}"
for i in range(n - 1):
    sum += (a * 10 + a)
    a = a * 10 + b
    gong_shi += f"+{a}"
print(f'{gong_shi} = {sum}')
