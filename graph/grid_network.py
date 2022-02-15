# https://www.acmicpc.net/problem/18769


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


def kruskal(edges):
    answer = 0
    edges.sort()
    parent = [i for i in range(r * c)]
    for cost, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        answer += cost
        union(parent, a, b)
    print(answer)


for tc in range(int(input())):
    r, c = map(int, input().split())
    edges = []
    for i in range(r):
        horizon_data = list(map(int, input().split()))
        for j, x in enumerate(horizon_data):
            num = i * c + j
            edges.append((x, num, num + 1))

    for i in range(r - 1):
        vertical_data = list(map(int, input().split()))
        for j, x in enumerate(vertical_data):
            num = i * c + j
            edges.append((x, num, num + c))

    kruskal(edges)
