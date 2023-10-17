# 1. 给定用于表示年、月、日的 3 个整数 y、m 和 d，判定该日期是该
# 年的第几天。
# 相关说明
# 输入条件 输入用于表示日期（年、月、日）的 3 个正整数 y、m 和 d，肯定是正整数，但是否属于合法的日期数据未知。
# 输出要求
# 返回值为整型，具体定义如下：
# 1) 如所给日期数据不合法，返回-1
# 2) 如所给日期数据合法，则返回该日期是该年的第几
# 天。以 2019-1-1 为例，该日期是 2019 年的第 1 天，
# 则返回 1
import re


def fun1(y, m, d):
    import calendar
    import datetime
    if m > datetime.datetime(y, 12, 1).month:
        return -1
    elif d > datetime.datetime(y, m, calendar.monthrange(y, m)[1]).day:
        return -1
    else:
        a = datetime.datetime(y, 1, 1)
        b = datetime.datetime(y, m, d)
        c = b - a
        return c.days + 1


# 2. 已知每只鸡有 2 只脚，每只兔子有 4 只脚，求解鸡兔同笼问题。
# 给定鸡和兔子的头的总数 m 和脚的总数 n。求鸡和兔子的数量。
# 相关说明
# 输入条件 给定 m 和 n 为整数。
# 输出要求
# 如果 m 和 n 中任何一个小于 0，返回 None。 如任何一个解不是整数，或任何一个解小于 0，返回 None。
# 返回元组(鸡的数量, 兔子的数量)
def fun2(m, n):
    if m < 0 or n < 0:
        return None
    else:
        hen = 2 * m - n / 2
        rabbit = n / 2 - m
        if hen < 0 or rabbit < 0:
            return None
        elif int(hen) + int(rabbit) != m:
            return None
        else:
            return (int(hen), int(rabbit))


# 3. 判定一个整数列表里的元素排序后能否构成等差数列
def fun3(lst):
    if len(lst) <= 1:
        return False
    else:
        lst.sort()
        delta = lst[1] - lst[0]
        for i in range(len(lst)):
            if lst[i] != lst[0] + i * delta:
                return False
        else:
            return True


# 4. 计算并返回整数列表的中位数。中位数的含义：对于一个有序的
# 数列，排列位置位于整个列表中间的那个元素的值即为中位数。
# 如果数列有偶数个值，取最中间的两个数值的平均数作为中位数。
# 相关说明
# 输入条件 给定 lst 为列表，不保证列表元素有序，不保证每个顶层元素都
# 是整数，也不保证列表中一定有元素。
# 输出要求
# 如果列表为空列表，返回 None。
# 如果列表的顶层元素出现整数以外的类型，返回 None。
# 对于非空的整数列表返回中位数（结果取整）。
def fun4(lst):
    length = len(lst)
    lst.sort()
    if length % 2 == 1:
        return lst[int(length / 2) + 1]
    else:
        if isinstance(lst[int(length / 2) - 1], int) and isinstance(lst[int(length / 2)], int):
            return int((lst[int(length / 2) - 1] + lst[int(length / 2)]) / 2)
        else:
            return None


# 5. 输入一个包含 3 到 11 个单词的字符串，单词与单词之间用空格分
# 开，其中的单词一定是 0-9 数字的英文单词（单词的字母可能大
# 写也可能小写）。请编写程序将其转换为阿拉伯数字的字符串。
# 相关说明
# 输入条件 给定 sentence 为字符串。
# 输出要求 返回电话号码字符串，如果输入的长度不合法则返回 None。
def fun5(sentence):
    s = str(sentence)
    s = re.sub('one', '1', s.lower())  # 优秀的代码需要易于使人理解
    s = re.sub('two', '2', s.lower())
    s = re.sub('three', '3', s.lower())
    s = re.sub('four', '4', s.lower())
    s = re.sub('five', '5', s.lower())
    s = re.sub('six', '6', s.lower())
    s = re.sub('seven', '7', s.lower())
    s = re.sub('eight', '8', s.lower())
    s = re.sub('nine', '9', s.lower())
    s = re.sub('\s', '', s)
    if 0 < len(s) <= 9:
        return s


# 6. 给定 4 个整数 a, b, c, d，求集合 s = {x / y | a <= x <= b, c <= y <= d}
# 中元素的个数
def fun6(a, b, c, d):
    lst = [x / y for x in range(a, b + 1) for y in range(c, d + 1)]
    return len(set(lst))


# 7. 输入两个字符串参数 s1, s2（均不为空字符串），和一个非零正整
# 数 n。请按照如下规则将字符串 s2 插入到 s1 中，并返回生成的字
# 符串：
# 1) s1 中每隔 n 个字符，插入一次 s2
# 2) 如果最后一次不足 n 个字符，则先用空格符号补全到 n 个字符，然后插入一
# 次 s2
# 相关说明
# 输入条件 s1, s2 均不为空字符串，n 为非零正整数
# 输出要求 返回结果字符串
def fun7(s1, s2, n):
    s3 = ''
    if len(s1) % n != 0:
        s1 += ' ' * (n - (len(s1) % n))
        print(s1)
    count = 0
    for i in s1:
        count += 1
        if count % n == 0 and count != 0:
            s3 += i
            s3 += s2
        else:
            s3 += i
    return s3


# 8. 给定一个字符串，找出其中“<tag>”形式的标签片段，并替换成
# “[TAG-len]”形式的片段。其中 tag 是由字母、数字和下划线构成
# 可变的标签文本，TAG 是将 tag 中的英文字母全部转换成大写字 母后的形式，len 是 TAG 的长度，详见测试用例。
# 相关说明
# 输入条件
# 给定 sentence 为字符串，不包含中文。字符串中可替换部分可
# 能出现 0 次或多次。
# 输出要求 返回经过替换的字符串。如没有需要替换的内容，则原样返回。
def fun8(s):  # 别问我在写什么，我也找不到fun8写了什么，反正能跑
    lst1 = re.findall('<.*?>', s)
    lst2 = []
    b = ''
    for i in lst1:
        a = re.sub('<', '', i)
        a = re.sub('>', '', a)
        for i in a:
            b += i.upper()
        TAG = f'[{b}-{len(b)}]'
        b = ''
        lst2.append(TAG)  # 仅在python3.6及以上的版本可使用f-string
    dic = {k: v for k, v in zip(lst1, lst2)}
    for i in dic.keys():
        s = re.sub(i, dic[i], s)
    return s
