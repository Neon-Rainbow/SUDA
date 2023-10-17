# 编写一个程序，产生两个在[5，20]之间的随机正整数 a 和 b。a 代表班级的女生人数，
# b 代表班级的男生人数，计算并输出女生占班级总人数的比例，要求输出比例结果采用
# 百分比形式，占 8 列，右对齐，保留 2 位小数
import random

a = random.randint(5, 20)  # 男生人数
b = random.randint(5, 20)  # 女生人数
percent = a/(a+b)
print(f'女生占班级总人数的比例为{percent:>8.2%}')