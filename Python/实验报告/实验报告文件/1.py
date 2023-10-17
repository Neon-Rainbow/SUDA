# 编写一个程序，提示用户从键盘输入一个 3 位整数，请编写程序计算三位整数的各位数
# 字之和，并输出到屏幕上，要求输出占 4 列，右对齐
num = input('输入一个三位整数')
sum = 0
for i in num:
    sum += int(i)
# 两种左对齐方式
print(str(sum).ljust(4))
print(f'{sum:>4}')