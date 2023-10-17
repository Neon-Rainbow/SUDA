#! /usr/bin/env python
# coding=utf-8

def get_current(input, i):
    return input[i]


def get_next(input, i):
    if i < len(input) - 1:
        return input[i + 1]
    else:
        return ''


def add_to_status(t0, ch, t1, s):
    s.append((t0, ch, t1))


def check_vocab(ch):
    if 'a' <= ch <= 'z':
        return True
    else:
        return False


def check_union(ch, i, input):
    if i < len(input) - 1:
        return input[i + 1] == '|'
    else:
        return False


def re2nfa(input):
    S = []  # Status
    ST = []  # temp status
    T = 0
    K = 0
    n = len(input)
    i = 0
    while i < len(input):
        ch = get_current(input, i)
        sym = get_next(input, i)

        if check_vocab(ch):
            if sym == '*':
                add_to_status(T, 'eps', K + 1, S)
                add_to_status(K + 1, ch, K + 1, S)
                add_to_status(K + 1, 'eps', K + 2, S)
                K = K + 2
                T = K
            elif check_union(ch, i, input):
                add_to_status(T, 'eps', K + 1, S)
                add_to_status(K + 1, ch, K + 2, S)
                add_to_status(K + 2, 'eps', K + 5, S)
                add_to_status(T, 'eps', K + 3, S)
                add_to_status(K + 3, get_next(input, i + 1), K + 4, S)
                add_to_status(K + 4, 'eps', K + 5, S)
                K = K + 5
                T = K
                i += 2  # skip next character
            else:
                add_to_status(T, ch, K + 1, S)
                K = K + 1
                T = K

        if ch == '(':
            ST.append(T)
            add_to_status(T, 'eps', K + 1, S)
            K = K + 1
            T = K

        if ch == ')':
            if sym != '*':
                pass
            else:
                add_to_status(T, 'eps', ST[-1], S)
                add_to_status(ST[-1], 'eps', K + 1, S)
                K = K + 1
                T = K
                ST.pop()
        i += 1
    return S


if __name__ == "__main__":
    print(re2nfa("(a|b)*"))
