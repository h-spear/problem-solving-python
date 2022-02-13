# https://www.acmicpc.net/problem/1774


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


n, m = map(int, input().split())
pos = [tuple(map(int, input().split())) for _ in range(n)]
edges = []
already_exist = [tuple(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        x1, y1 = pos[i - 1]
        x2, y2 = pos[j - 1]
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        if (i, j) in already_exist:
            union(parent, i, j)
            continue
        edges.append((dist, i, j))


def kruskal():
    answer = 0
    edges.sort()
    for cost, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        answer += cost
        union(parent, a, b)
    print("{:.2f}".format(answer))


kruskal()
