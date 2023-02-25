# https://www.acmicpc.net/problem/1368

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
edges = []
for i in range(n):
    edges.append((int(input()), 0, i + 1))

for i in range(n):
    input_data = list(map(int, input().split()))
    for j in range(i + 1, n):
        edges.append((input_data[j], i + 1, j + 1))


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
    answer = 0
    edges.sort()
    parent = [i for i in range(n + 1)]
    for c, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        answer += c
        union(parent, a, b)
    print(answer)


kruskal()
