# https://www.acmicpc.net/problem/10775

import sys

input = lambda: sys.stdin.readline().rstrip()


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b


parent = [0] * 100001
for i in range(1, 100001):
    parent[i] = i

g = int(input())
p = int(input())
plane = []
for _ in range(p):
    plane.append(int(input()))

cnt = 0
for gi in plane:
    x = find(parent, gi)
    if x == 0:
        break
    union(parent, x, x - 1)
    cnt += 1

print(cnt)
