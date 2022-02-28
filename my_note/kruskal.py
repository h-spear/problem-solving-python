import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
m = int(input())
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
    answer = 0

    for c, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue

        answer += c
        union(parent, a, b)

    print(answer)


kruskal()
