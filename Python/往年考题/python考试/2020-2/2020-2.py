# 2020-2
# 1. 求一个正整数（大于零的整数）除了 1 和它本身以外的升序排列的因数列表。
import math


def fun1(n):
    lst = []
    for i in range(2, n):
        if n % i == 0:
            lst.append(i)
    return lst


# 2. 求 a 和 b 两个正整数（大于零的整数）除了 1 以外的升序排列的公因数列表。
def fun2(a, b):
    lst = []
    for i in range(2, min(a, b) + 1):
        if a % i == b % i == 0:
            lst.append(i)
    return lst


# 3. 求列表的中位数。中位数是按升序或降序排列的一组数据中居于中间位置的数。如
#    有偶数个数据，则取中间两个数的平均值的取整值为中位数。
# 相关说明
# 输入条件 参数 lst 是一个整数列表，元素个数未知，无序。
# 输出要求 如果 lst 是空列表，则返回 None，否则返回题意要求的中位数。
# 其它要求 将代码写入函数 func3。
def fun3(lst):
    length = len(lst)
    lst.sort()
    if length % 2 == 1:
        return lst[int(length / 2)]
    else:
        return (lst[int(length / 2) - 1] + lst[int(length / 2)]) / 2


# 4. 求列表中有几个值有重复值。
def fun4(lst):
    dic = {}
    count = 0
    for i in lst:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    for i in dic.keys():
        if dic[i] > 1:
            count += 1
    return count


# 5. 给定正整数 n，求[2, n)内的所有回文质数（既是质数又是回文数）构成的降序列表
def fun5(n):
    lst = []

    def is_prime(num):
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

    def hui_wen(num):
        if str(num) == str(num)[::-1]:
            return True
        else:
            return False

    for i in range(2, n):
        if is_prime(i) and hui_wen(i):
            lst.append(i)
    lst.sort(reverse=True)
    return lst


print(fun5(11))


# 6. 求一个集合中有多少个整数可以表达为该集合中另外两个整数的和。
# 相关说明
# 输入条件 参数 s 是一个整数集合。
# 输出要求 可以表达为该集合中另外两个整数的和的整数个数。
# 其它要求 将代码写入函数 func6。

def fun6(s):  # 啥都不想管，直接三个for循环遍历，简洁明了。
    s = set(s)
    s = list(s)
    count = 0
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s) - 1):
            for k in range(j + 1, len(s)):
                if s[i] == s[j] + s[k] or s[j] == s[i] + s[k] or s[k] == s[i] + s[j]:
                    count += 1
    return count


# 7. 给定一个字符串，将字符串正中间的 4 个字符改成“****”。如字符串长度为奇数，
# 则扣除（不是删除）字符串尾部的 1 个字符后确定字符串正中间的位置。
# 相关说明
# 输入条件 参数 s 是一个字符串。
# 输出要求 返回正中间的 4 个字符被改成“****”的字符串。如字符串长度小于 6
# 或大于 10，则返回“****”。
# 其它要求 将代码写入函数 func7。
def fun7(s):
    if len(s) < 6 or len(s) > 10:
        return '****'
    else:
        return s[:len(s) // 2 - 2] + '****' + s[len(s) // 2 + 2:]


# 8. 已知一个等差数列缺失了一个值，求出这个缺失值。
# 输入条件 参数 lst 是一个未排序整数列表。缺失值一定不在数列的两端。
# 输出要求 返回一个缺失的值，可使得 lst 构成等差数列。如 lst 长度小于 4，则返回 None。
def fun8(lst):
    lst.sort()
    delta = (lst[-1] - lst[0]) / (len(lst))
    if len(lst) < 4:
        return None
    else:
        for i in range(len(lst)):
            if lst[i] != lst[0] + delta * i:
                return int(lst[0] + delta * i)
