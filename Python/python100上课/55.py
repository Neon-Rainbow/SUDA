a = '10100101'
count = 0
sum = 0
for i in a:
    sum += int(i)
    if i == '0':
        count += 1
print(f"有{count}个0\n数字之和为{sum}")