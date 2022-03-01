# https://www.acmicpc.net/problem/1629

import sys

input = sys.stdin.readline
a, b, c = map(int, input().rstrip().split())


def pow(C, n, mod):
    res = 1
    while n:
        if n & 1:
            res = res * C
        C = C * C % mod
        n >>= 1
    return res % mod


print(pow(a, b, c))
