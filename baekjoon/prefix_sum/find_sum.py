# https://www.acmicpc.net/problem/11441

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
m = int(input())
sa = [0] * (n + 1)
for i in range(1, n + 1):
    sa[i] = sa[i - 1] + a[i - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(sa[j] - sa[i - 1])
