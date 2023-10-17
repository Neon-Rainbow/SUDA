import re


# 2020-3
# 1. 求一个十进制正整数的二进制形式中 1 的个数。例如：6 的二进制为 110，其中 1
# 的个数为 2。
# 相关说明
# 输入条件 参数 num 是一个整数。
# 输出要求 如 num 是负数，返回 None，否则返回 1 的个数
# 其它要求 将代码写入函数 func1
def fun1(num):
    if int(num) < 0:
        return None
    else:
        num2 = bin(num)
        return num2.count('1')


# 2. 给定一个元素全部是整数的列表 lst，如果有一对数字（i，j），满足 lst[i]等于 lst[j]
# 并且 i 小于 j，那么 i 和 j 可以称为一个好数对，请返回 lst 的好数对的个数。
# 相关说明
# 输入条件 参数输入一个合法
# 输出要求 返回一个整数
# 其它要求 将代码写入函数 func2
def fun2(lst):
    count = 0
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length):
            if lst[i] == lst[j]:
                count += 1
    return count


# 3. 给定一个列表，包含整数、字符串、浮点数三种类型的元素。不同类型之间比较的
# 规则：字符串>浮点数>整数；同类型元素之间则正常比较。请按照大小规则对列表
# 从大到小排序，返回排序后的列表。
# 相关说明
# 输入条件 列表，包含整数、字符串、浮点数三种类型元素。
# 输出要求 按照规则返回排序后的列表。
# 其它要求 将代码写入函数 func3
def fun3(lst):
    length = len(lst)
    for i in range(length):
        for j in range(i+1,length):
            pass
    pass


# 4. 给定一个字符串，单词与单词之间以空格划分（不含标点符号,区分大小写），请用
# 字典统计文本中各个单词出现的次数，即字典的 key 为字符串中的单词，value 为
# 该单词出现的次数，返回该字典。
# 相关说明
# 输入条件 字符串文本，单词与单词之间以空格间隔，不包含标点。
# 输出要求 统计各个单词出现的次数，返回字典。
# 其它要求 将代码写入函数 func4
def fun4(s):
    word = re.compile('[A-Za-z]+')
    word_list = re.findall(word, s)
    dic = {}
    for i in word_list:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    return dic


# 5. 给定一个字符串和一个正整数 n，字符串只包含英文字母或数字，如果 n 大于等于
# 10，则先让 n 对 10 取余赋值给 n，然后将字符串中的所有英文字母转换成其后面
# 第 n 个字符。如果大写字母后面的第 n 个字符超过了大写字母’Z’，则从大写’A’接着
# 计数，如果小写字母后面的第 n 个字符超过了小写字母’z’，则从小写’a’接着计数，
# 保证转换后的字符仍然是英文字母。例如：当 n 为 5 时，则’V’->’A’，‘W’->’B’，‘X’->’C’,
# ‘Y’->’D’，’Z’->’E’,’v’->’a’，‘w’->’b’，‘x’->’c’, ‘y’->’d’，’z’->’e’。
# 相关说明
# 输入条件 字符串 s 和正整数 n
# 输出要求 返回转换后的字符串。
# 其它要求 将代码写入函数 func5
def fun5(s, n):
    s2 = ''
    while n >= 10:
        n = n % 10
    char_dict1 = {chr(i): (i - 65) for i in range(65, 91)}
    char_dict2 = {chr(i): (i - 97) for i in range(97, 123)}

    def exchange(letter):
        a = str(letter)
        ascii_a = ord(a)
        # print(f'调试点1:{ascii_a}')
        if a.isupper():
            ascii_a = ascii_a + n - 65
            # print(f'调试点2:{ascii_a}')
            while ascii_a > 25:
                ascii_a -= 26
            # print(f'测试点4 转换后的顺序{ascii_a}')
            for k, v in char_dict1.items():
                if v == ascii_a:
                    return k
        elif a.islower():
            ascii_a = ascii_a + n - 97
            # print(f'调试点3:{ascii_a}')
            while ascii_a > 25:
                ascii_a -= 26
            # print(f'测试点4 转换后的顺序{ascii_a}')
            for k, v in char_dict2.items():
                if v == ascii_a:
                    return k
        elif a.isdigit():
            return a

    for i in s:
        lett = exchange(i)
        s2 += lett
        # print(f'测试点（查看每个元素转换情况）{i} : {lett}')
    return s2


print(fun5('uvW1122xyz', 5))


# 6. 给定一个包含若干电话号码的字符串，其中电话号码由 3 或 4 位区号和 7 或 8 位电
# 话组成，提取所有电话号码组成列表并返回该列表。
# 相关说明
# 输入条件 字符串 s，s 中不会出现两个电话号码相邻出现
# 输出要求
# 返回电话号码组成的列表,如果字符串中没有符合要求的电话
# 号码，则返回空列表
# 其它要求 将代码写入函数 func6
def fun6(s):
    a = re.compile('[0-9]{3,4}-[0-9]{7,8}')
    lst = re.findall(a, s)
    return lst


# 7. 给定一个二维列表 lst，该列表存储了如下图(a)所示的矩阵，以矩阵的对角线(下图
# 红色线条)为轴进行翻转得到下图(b)，将图(b)中的所有元素减去对角线上的最小值
# 即可得到图(c)所示的矩阵。最后，以二维列表的形式返回最终的矩阵。本例中图(a)
# 与(b)对应的二维列表分别是[[1,2,8],[4,5,9],[7,2,6]]和[[1,4,7],[2,5,2],[8,9,6]]，对角线上
# 的最小值是 1，返回结果对应的二维列表是[[0,3,6],[1,4,1],[7,8,5]]。
# 相关说明
# 输入条件 矩阵中的元素都是整数，矩阵的行数与列数相等并且大于等于 2
# 输出要求 以二维列表的形式返回最终矩阵
# 其它要求 将代码写入函数 func7
def fun7(lst):
    lst2 = []
    lst3 = [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]
    for i in range(len(lst3)):
        lst2.append(lst3[i][i])
    minimum = min(lst2)
    for i in range(len(lst3)):
        for j in range(len(lst3)):
            lst3[i][j] -= minimum
    return lst3


# 8. 给定一个由元组构成的列表𝐿𝐿，其中每个元组由 2 个 0 至 99 之间的整数元素构成。
# 设有两个元组𝑡𝑡1和𝑡𝑡2，如果𝑡𝑡1中的元素都不比𝑡𝑡2中对应（同一位置）的元素大，且𝑡𝑡1
# 中至少存在一个元素比𝑡𝑡2中对应元素小，则称𝑡𝑡1支配𝑡𝑡2。保留𝐿𝐿中所有不被任何元组
# 支配的元组，并将𝐿𝐿按元组第 1 个元素从小到大的顺序排列。返回排序后的列表𝐿𝐿。
def fun8():
    pass
