import sys
from functools import cache
from typing import List

# 由于使用了递归,递归树最大深度过大,导致内存过大

def solve(a: List[int]) -> int:
    n = len(a)

    @cache
    def min_deletions(i):
        if i >= n:
            return 0
        min_ops = min_deletions(i + 1) + 1
        next_index = i + a[i]
        if next_index < n:
            min_ops = min(min_ops, min_deletions(next_index + 1))
        return min_ops
    return min_deletions(0)


def main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    main()
