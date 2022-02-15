# https://www.acmicpc.net/problem/17490

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 5)
from collections import defaultdict

n, m, k = map(int, input().split())
s = list(map(int, input().split()))
parent = [i - 1 for i in range(n + 1)]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


# **********************
# 공사중인 경로가 1개여도 무조건 YES
if m <= 1:
    print("YES")
    exit(0)
if k == 0:
    print("NO")
    exit(0)

for _ in range(m):
    i, j = map(int, input().split())
    if i == n:
        parent[1] = 1
        continue
    parent[j] = j


group = defaultdict(lambda: 1000001)
for i in range(1, n + 1):
    x = find(parent, i)
    group[x] = min(group[x], s[i - 1])
if sum(group.values()) <= k:
    print("YES")
else:
    print("NO")
