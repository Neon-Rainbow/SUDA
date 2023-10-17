import math


def func1(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def func2(num):
    return int(str(num)[1])


def func3(m):
    if m <= 0:
        return
    elif 0 < m < 10000:
        return (20000 + m * 5) / m
    return (50000 + m * 3) / m


def func4(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return
    if x == y == z:
        return 1
    lst = [x, y, z]
    lst.sort()
    if lst[0] + lst[1] <= lst[2]:
        return
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        return 2
    return 3


def func5(n, m):
    return sum((x for x in range(n, m + n + 1) if x % 2 == 0))


def isHalfPrime(num):
    cnt = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    return False


def func6(n):
    return sum(filter(isHalfPrime, range(10, n + 1)))


def func7(lst):
    return list(filter(lambda x: x % 2 != 0, lst)) + list(filter(lambda x: x % 2 == 0, lst))


def func8(lst):  # Solution 1
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] in lst[:i]:
            del lst[i]
    return lst


def func8_solution2(lst):  # Solution 2
    visited = set()
    res = []
    for i in range(len(lst)):
        if lst[i] not in visited:
            res.append(lst[i])
            visited.add(lst[i])
    return res


if __name__ == "__main__":
    pass