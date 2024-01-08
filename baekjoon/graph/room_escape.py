# https://www.acmicpc.net/problem/23743

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


def topologySort(n, edges):
    edges = sorted(edges)

    parent = [i for i in range(n + 1)]

    mstLength = 0
    for c, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        mstLength += c
        union(parent, a, b)

    return mstLength


N, M = map(int, input().split())

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

t = list(map(int, input().split()))

for i in range(1, N + 1):
    edges.append((t[i - 1], 0, i))

print(topologySort(N, edges))
