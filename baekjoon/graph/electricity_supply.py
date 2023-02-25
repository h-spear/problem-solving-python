# https://www.acmicpc.net/problem/10423

import sys

input = lambda: sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
plant = list(map(int, input().split()))
edges = []
parent = [i for i in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()


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


def check_supply(a):
    for p in plant:
        if find(parent, a) == find(parent, p):
            return True
    return False


def kruskal():
    answer = 0
    for cost, a, b in edges:
        if check_supply(a) and check_supply(b):
            continue
        if find(parent, a) == find(parent, b):
            continue
        answer += cost
        union(parent, a, b)

    print(answer)


kruskal()
