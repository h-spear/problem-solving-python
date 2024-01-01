# https://www.acmicpc.net/problem/1351

import sys

input = lambda: sys.stdin.readline().rstrip()

N, P, Q = map(int, input().split())
cache = {}


def dp(i):
    if i == 0:
        return 1
    if i in cache:
        return cache[i]

    cache[i] = dp(i // P) + dp(i // Q)
    return cache[i]


print(dp(N))
