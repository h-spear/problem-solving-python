# https://www.acmicpc.net/problem/16398

n = int(input())
edges = []
parent = [i for i in range(0, n + 1)]
for i in range(n):
    cost = list(map(int, input().split()))
    for j in range(i + 1, n):
        edges.append((cost[j], i, j))

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


def kruskal():
    answer = 0
    for cost, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        answer += cost
        union(parent, a, b)

    print(answer)


kruskal()
