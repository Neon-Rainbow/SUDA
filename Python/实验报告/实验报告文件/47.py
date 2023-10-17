i = int(input('存款金额为'))
if i < 100000:
    sum = i * 1.015
elif 100000 <= i < 500000:
    sum = i * 1.02
elif 500000 <= i < 100000:
    sum = i * 1.03
elif 1000000 <= i:
    sum = i * 1.035
print(sum)
