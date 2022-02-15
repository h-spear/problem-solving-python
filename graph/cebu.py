# https://www.acmicpc.net/problem/13905

import sys

# recursion 제한을 풀어야 통과함.
sys.setrecursionlimit(10 ** 7)
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
s, e = map(int, input().split())
edges = []
parent = [i for i in range(n + 1)]
for _ in range(m):
    h1, h2, k = map(int, input().split())
    edges.append((k, h1, h2))


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
    answer = float("inf")
    edges.sort(reverse=True)
    for weight, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        answer = min(weight, answer)
        union(parent, a, b)

        if find(parent, s) == find(parent, e):
            print(answer)
            return
    print(0)


kruskal()
