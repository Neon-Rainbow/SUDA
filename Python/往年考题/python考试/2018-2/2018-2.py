import math
import re
import numpy as np


# 2018-2
# 1. 给定整数 m 和 n，如果 m 和 n 都大于 1，则判定 m 和 n 是否互质，并返回判定结 果。
def fun1(m, n):
    if m < 1 or n < 1:
        return False
    else:
        for i in range(2, min(m, n)):
            if m % i == 0 and n % i == 0:
                return False
        else:
            return True


# 2. 一个整数列表 L=[a1, a2, …, an]中，如果一对数(ai, aj)满足 ai>aj 且 i<j，那么这对数就
# 称为一个逆序，列表 L 中逆序的数量称为逆序数。求一个整数列表 L 的逆序数
def fun2(lst):
    length = len(lst)
    count = 0
    for i in range(length - 1):
        for j in range(i + 1, length):
            if lst[i] > lst[j]:
                count += 1
    return count


# 3. 矩阵相乘： 输入两个整数类型的矩阵 mat1（m 行 d 列）和 mat2（d 行 n 列），返
# 回矩阵相乘后的结果 mat1*mat2（m 行 n 列）。矩阵均用二维列表进行表示
def fun3(A, B):
    A_row, A_col = len(A), len(A[0])
    result = []
    BT = [list(row) for row in zip(*B)]
    for Ai in range(A_row):
        rowItem = []
        for Bi in range(len(BT)):
            num = 0
            for Bj in range(len(BT[Bi])):
                num += A[Ai][Bj] * BT[Bi][Bj]
            rowItem.append(num)
        result.append(rowItem)
    return result


def fun3_using_numpy(mat1, mat2):
    arr1 = np.array(mat1)
    arr2 = np.array(mat2)
    print(arr1)
    print(arr2)
    return np.multiply(arr1, arr2)


# 4. 一维列表转成二维列表： 输入一个长度为 n*n 的一维列表， 返回一个 n 行 n 列的
# 二维列表。
def fun4(lst):
    n = int(math.sqrt(len(lst)))
    lst2 = [[0 for i in range(n)] for i in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            lst2[i][j] = lst[count]
            count += 1
    return lst2


# 5. 给定一个字符串，包含了若干个以空格分开的单词，统计其中每个单词出现的次数，
# 以列表的形式返回其中出现次数最多的三个单词（三者按照出现次数降序排序，当
# 出现次数相同时，对单词按照字典序降序排序），如果不足三个单词，则按照上述
# 规则排序后全部返回。
def fun5(s):
    a = re.compile('[a-zA-Z]+')
    lst = re.findall(a, s)
    dic = {}
    lst2 = []
    for i in lst:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    dic2 = dict(sorted(dic.items(), key=lambda r: (r[1], r[0]), reverse=True))
    for i in dic2.keys():
        lst2.append(i)
    return lst2


def fun5_using_collections(s):
    from collections import Counter
    a = re.compile('[a-zA-Z]+')
    lst = re.findall(a, s)
    counts = Counter(lst)
    print(counts)
    top_three = counts.most_common(3)
    return top_three


# 6. 仅包含小写字母的两个单词 S 和 T 的 Jaccard 系数（记为 J）由如下三个统计量来确
# 定：令 a 是在两个单词中都出现的字母的个数，b 是在 S 中出现但没有在 T 中出现
# 的字母的个数，c 是在 T 中出现但没有在 S 中出现的字母的个数，那么 J = a / (a + b +
# c)。给定两个单词 S 和 T，求确定其 Jaccard 系数的三个统计量 a,b,c。
def fun6(s, t):
    set_s = set(s)
    set_t = set(t)
    a = len(set_s & set_t)
    b = len(set_s - set_t)
    c = len(set_t - set_s)
    return (a, b, c)


# 7. 统计一个非空字符串中出现次数最多的字符及其出现次数。其中英文字母不区分大
# 小写，全部统计为大写字母，如’a’和’A’在计数时进行合并为’A’。结果以包含字符和
# 对应次数的列表形式进行返回。数据中不存在并列最多的情况，该情况不需要考虑。
# 相关说明
# 输入条件
# 能保证目标字符串非空、且其中不存在出现次数并列最多的字符
# 输出要求 结果以包含字符和对应次数的列表形式进行返回。
# 其它要求 将代码写入函数 func7
def fun7(s):
    dic = {}
    for i in s.upper():
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    return sorted(dic.items(), key=lambda a: a[1], reverse=True)[0]


# 8. 一个字符串中存在多个正整数，请提取出位数在[3,5]之间的所有正整数，构成一个
# 列表，对此列表按照数字和平均值（各位数字的总和/位数）进行降序排序，并返回
# 排序结果列表。数字和平均值就是各位数字的总和除以位数，例如 2345 的数字和平
# 均值=(2+3+4+5)/4=3.5，12 的数字和平均值=(1+2)/2=1.5。
# 相关说明
# 输入条件 存在多个正整数的字符串
# 输出要求
# 结果以满足要求的列表形式进行返回。如原字符串中不存
# 在满足条件的正整数，返回 None
# 其它要求 将代码写入函数 func8
def fun8(s):
    num = re.compile('[0-9]{3,5}')
    lst = re.findall(num, s)
    lst.sort(key=lambda x: sum(list(map(int, list(x)))) / len(x), reverse=True)
    return list(map(int, lst))
