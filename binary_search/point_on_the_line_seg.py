# https://www.acmicpc.net/problem/11663

import sys
from bisect import bisect_left, bisect_right

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
point = sorted(list(map(int, input().split())))
for _ in range(m):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    print(bisect_right(point, b) - bisect_left(point, a))
