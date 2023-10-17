import random

a = random.randint(0,100)
b = random.randint(0,100)
c = int(input(f"{a} + {b} ="))
if c == a+b:
    print(f"正确")
else:
    print(f"错误\n正确答案是{a} + {b} = {a+b}")