def func1(x):
    if x >= 0:
        y = 5 * x
    else:
        y = 3 * abs(x) + 1
    return y


def func2(x):
    if x >= 10:
        y = 10
    elif 8 <= x < 10:
        y = 8 * x ** 3
    elif 3 <= x < 8:
        y = 3 * x ** 2
    elif 0 <= x < 3:
        y = x - 1
    else:
        y = abs(x)
    return y


def func3(m, n):
    if m <= n:
        num = list(range(m, n + 1))
        sum = 0
        for i in range(len(num)):
            if num[i] % 2 != 0:
                sum += num[i]
        return sum
    else:
        return None


def func4(m, n):
    num = list(range(m, n + 1))
    sum = 0
    for i in range(len(num)):
        sum += list(map(int, list(str(num[i])))).count(2)
    return sum


def func5(num):
    if num > 0:
        numlist = list(map(int, list(str(num))))
        return [len(numlist), sum(numlist), max(numlist)]
    else:
        return None


def func6(m, n):
    if m > 0 and n > 0:
        if m < 100:
            return m
        else:
            mlist = list(map(int, list(str(m))))
            mlist[0] = (mlist[0] + n) % 10
            return int(''.join(list(map(str, mlist))))
    else:
        return None


def func7(k, lst):
    if k <= len(lst):
        lst[:k] = reversed(lst[:k])
    else:
        lst.reverse()
    return lst


def func8(v, lst):
    for i in range(len(lst) - 1, -1, -1):
        d = sum(list(map(int, list(str(lst[i]))))) / len(str(lst[i]))
    if d < v:
        del lst[i]
    lst.sort(reverse=True)
    return lst


if __name__ == "__main__":
    pass
