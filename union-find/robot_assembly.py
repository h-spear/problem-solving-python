# https://www.acmicpc.net/problem/18116

import sys

input = lambda: sys.stdin.readline().rstrip()


def find(parent, x):
    if parent[x] < 0:
        return x

    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a == b:
        return

    if parent[a] < parent[b]:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b


n = int(input())
parent = [-1 for _ in range(1000011)]

for _ in range(n):
    cmd, *i = input().split()

    if cmd == "I":
        union(parent, int(i[0]), int(i[1]))
    else:
        x = find(parent, int(i[0]))
        print(-parent[x])
