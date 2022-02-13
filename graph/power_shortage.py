# https://www.acmicpc.net/problem/6497

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
    else:
        parent[a] = b


while 1:
    m, n = map(int, input().split())

    if m == n == 0:
        break

    edges = []
    parent = [i for i in range(n + 1)]
    answer = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        answer += z
        edges.append((z, x, y))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find(parent, a) == find(parent, b):
            continue
        answer -= cost
        union(parent, a, b)
    print(answer)
