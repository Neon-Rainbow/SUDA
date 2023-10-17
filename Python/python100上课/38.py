a = int(input("请输入不超过5位的正整数"))
a = str(a)
print(f"{a}是{len(a)}位数")
for i in a:
    print(i)
print(f"逆序数为{a[::-1]}")