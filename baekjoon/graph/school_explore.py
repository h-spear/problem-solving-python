# https://www.acmicpc.net/problem/13418

import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
edges = []
for _ in range(m + 1):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))


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


def kruskal(rev=False):
    parent = [i for i in range(n + 1)]
    k = 0
    edges.sort(reverse=rev)
    for c, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        k += 1 - c
        union(parent, a, b)
    return k ** 2


print(kruskal() - kruskal(True))
