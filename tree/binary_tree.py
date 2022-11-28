# https://www.acmicpc.net/problem/13325

import sys

input = lambda: sys.stdin.readline().rstrip()
k = int(input())
w = list(map(int, input().split()))
w.insert(0, 0)
w.insert(0, 0)
n = 1 << k + 1


def dfs(x):
    if x >= n:
        return

    dfs(2 * x)
    dfs(2 * x + 1)
    if 2 * x + 1 <= n:
        l = w[2 * x]
        r = w[2 * x + 1]
        m = max(l, r)
        w[2 * x] = m
        w[2 * x + 1] = m
        w[x] += m


dfs(1)

for i in range(1 << k):
    w[i] -= w[2 * i]

print(sum(w))
