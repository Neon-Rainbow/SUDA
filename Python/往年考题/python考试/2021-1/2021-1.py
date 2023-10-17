# 2021-1
# 1.给定两个整数，判定这两个整数是否互质。
#
# 相关说明
# 输入条件	参数a、b是两个整数。
#           输入的两数确定是整数，无需考虑不是整数的情况。
#           两个整数的大小关系未知。
# 输出要求	如果两数互质，返回True，否则返回False。
#           如果a、b中任何一个数小于等于0，则返回False。
import math


def fun1(a, b):
    if a < 0 or b < 0:
        return False
    else:
        for i in range(2, min(a, b)):
            if a % i == 0 and b % i == 0:
                return False
        return True


# 2.输入一个正整数num，返回num的中间那位数字。
#
# 相关说明
# 输入条件	参数num是一个整数。
#           输入参数确定是正整数，不用考虑非正整数的情况。
# 输出要求	输出一位整数。不是输出字符串。
#           如果输入的整数有奇数位数字，则返回中间那位数。
#           如果输入的整数有偶数位数字，返回False。
def fun2(num):
    str_num = str(num)
    length = len(str_num)
    if length % 2 != 0:
        return str_num[int(length / 2)]
    else:
        return False


# 3.奶茶店的奶茶10元一杯，现在促销买5杯送3杯，买3杯送1杯，现有n元，计算最多可以买多少杯。
#
# 相关说明
# 输入条件	n一定是一个正整数。
# 输出要求	返回一个整数表示奶茶的杯数。
# 其它要求	将代码写入函数func3
def fun3(n):
    cup = int(n / 10)
    lst = [0]
    for a in range(cup + 1):
        for b in range(cup + 1):
            for c in range(cup + 1):
                if 5 * a + 3 * b + c == cup:
                    lst.append(8 * a + 4 * b + c)
                    print(lst)
    return max(lst)


# 4.给定三个整数r、x、y表示圆的半径和一个点的x、y坐标，判断这个点和以（0,0）为圆心且半径为r的圆的关系。
#
# 相关说明
# 输入条件	参数r、x、y是三个整数。
#           不保证r、x、y为正整数。
# 输出要求	如果r、x、y中任何一个小于等于0，则返回False。
#           如果点在圆内部，则返回1。
#           如果点在圆周上，则返回2。
#           如果点在圆外部，则返回3。
# 其它要求	将代码写入函数func4
def fun4(r, x, y):
    if x < 0 or y < 0 or r < 0:
        return False
    else:
        length = math.sqrt(x ** 2 + y ** 2)
        if abs(float(r) - length) <= 0.000001:
            return 2
        elif float(r) - length < 0:
            return 3
        elif float(r) - length > 0:
            return 1


# 5.给定两个正整数n和m，求n到m范围内（含n和m）所有回文数的个数。所谓回文数就是将各位数字反向排列所得自然数与自己相等的数。
# 相关说明
# 输入条件	参数n和m都是正整数。
#           n和m的大小关系未知。
# 输出要求	返回回文数的个数。
# 其它要求	将代码写入函数func5
def fun5(n, m):
    count = 0
    for i in range(min(n, m), max(n, m) + 1):
        if str(i) == str(i)[::-1]:
            count += 1
    return count


# 6.给定一个正整数n，求n!末尾有多少个连续的0。
#
# 相关说明
# 输入条件	参数n为正整数
# 输出要求	返回n!末尾连续0的个数。
# 其它要求	将代码写入函数func6
def fun6(n):
    def factorial(num):
        if num == 1:
            return 1
        else:
            return num * factorial(num - 1)

    a = str(factorial(n))[::-1]
    count = 0
    for i in a:
        if i == '0':
            count += 1
        else:
            break
    return count


# 7.给定一个正整数列表lst，请将列表中元素重新排序。奇数集中存放在列表首部，偶数集中存放在列表尾部，奇数增序排列，偶数降序排列。返回一个重新排序列表。
#
# 相关说明
# 输入条件	参数lst是正整数列表。
#           所有元素均为正整数，无需额外的检查。
# 输出要求	返回重新排序的列表。
#           如果列表为空，返回空列表。
# 其它要求	将代码写入函数func7
def fun7(lst):
    lst1 = []
    lst2 = []  # lst1存放奇数，lst2存放偶数
    for i in lst:
        if i % 2 == 1:
            lst1.append(i)
        else:
            lst2.append(i)
    lst1.sort(reverse=False)
    lst2.sort(reverse=True)
    return lst1 + lst2


# 8.给定一个整数列表，求其中出现次数最多的元素。
#
# 相关说明
# 输入条件	参数lst是整数列表。
#           所有元素均为整数，无需额外的检查。
# 输出要求	如果只有一个元素出现次数最多，则返回一个整数，即为该元素。
#           如果出现次数最多的元素有多个，则返回这些元素构成的列表。返回的列表按降序排列。
# 其它要求	将代码写入函数func8
def fun8(lst):
    dic = {}  # 创建字典用于计算每个整数出现的次数
    lst2 = []  # 创建列表用于存放最后输出的结果
    lst3 = []  # 创建列表用于存放字典中的值
    for i in lst:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for k, v in dic:
        lst3.append(v)
        if lst3[0] == lst3[-1]:
            lst2.append(k)
    lst2.sort(reverse=True)
    if len(lst2) == 1:
        return lst2[0]
    else:
        return lst2
