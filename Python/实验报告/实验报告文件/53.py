import random

test_count = 1
a = random.randint(0,100)
while a != 50:
    test_count += 1
    a = random.randint(0, 100)
print(f"一共随机生成了{test_count}次")