# https://www.acmicpc.net/problem/17425

import sys

input = lambda: sys.stdin.readline().rstrip()
m = 1000003
f = [0] + [1] * m
g = [0] * (m + 1)
for i in range(2, m + 1):
    j = 1
    while i * j < m:
        f[i * j] += i
        j += 1

for i in range(1, m + 1):
    g[i] = f[i] + g[i - 1]

for t in range(int(input())):
    n = int(input())
    print(g[n])
