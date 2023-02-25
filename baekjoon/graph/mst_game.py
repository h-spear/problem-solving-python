# https://www.acmicpc.net/problem/16202

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
edges = []
for w in range(1, m + 1):
    a, b = map(int, input().split())
    edges.append((w, a, b))


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


def kruskal():
    parent = [i for i in range(n + 1)]
    result = 0
    cnt = 0
    for w, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        result += w
        cnt += 1
        union(parent, a, b)

    if cnt == n - 1:
        print(result, end=" ")
    else:
        print(0, end=" ")


edges.sort()
edges = deque(edges)
for _ in range(k):
    kruskal()
    edges.popleft()
