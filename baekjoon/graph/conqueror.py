# https://www.acmicpc.net/problem/14950

import sys

input = lambda: sys.stdin.readline().rstrip()

n, m, t = map(int, input().split())
edges = []
parent = [i for i in range(n + 1)]
for _ in range(m):
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


def kruskal():
    edges.sort()
    cnt = 0
    answer = 0
    for c, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        answer += c + cnt * t
        union(parent, a, b)
        cnt += 1
    print(answer)


kruskal()
