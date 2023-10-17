#! /usr/bin/env python
# coding=utf-8


S = []  # Status
ST = []  # temp status
T = 0
K = 0

input = 'a(a|b)*c'
n = len(input)


def get_current(input, i):
    return input[i]


def get_next(input, i):
    if i < len(input) - 1:
        return input[i + 1]
    else:
        return ''


def add_to_status(t0, ch, t1):
    S.append((t0, ch, t1))


def check_vocab(ch):
    if 'a' <= ch <= 'z':
        return True
    else:
        return False


def check_union(ch):
    if i < len(input) - 1:
        return input[i + 1] == '|'
    else:
        return False


i = 0
while i < len(input):
    ch = get_current(input, i)
    sym = get_next(input, i)

    if check_vocab(ch):
        if sym == '*':
            add_to_status(T, 'eps', K + 1)
            add_to_status(K + 1, ch, K + 1)
            add_to_status(K + 1, 'eps', K + 2)
            K = K + 2
            T = K
        elif check_union(ch):
            add_to_status(T, 'eps', K + 1)
            add_to_status(K + 1, ch, K + 3)
            add_to_status(K + 3, 'eps', K + 5)
            add_to_status(T, 'eps', K + 2)
            add_to_status(K + 2, get_next(input, i + 1), K + 4)
            add_to_status(K + 4, 'eps', K + 5)
            K = K + 5
            T = K
            i += 2  # skip next character
        else:
            add_to_status(T, ch, K + 1)
            K = K + 1
            T = K

    if ch == '(':
        ST.append(T)
        add_to_status(T, 'eps', K + 1)
        K = K + 1
        T = K

    if ch == ')':
        if sym != '*':
            pass
        else:
            add_to_status(T, 'eps', ST[-1])
            add_to_status(ST[-1], 'eps', K + 1)
            K = K + 1
            T = K
            ST.pop()
    i += 1

print(f"输入的字符串为{input}")
for t0, ch, t1 in S:
    print('%s\t[%s]\t%s' % (t0, ch, t1))
