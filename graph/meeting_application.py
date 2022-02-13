# https://www.acmicpc.net/problem/14621

n, m = map(int, input().split())
univ = list(input().split())
edges = []
parent = [i for i in range(n + 1)]
for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))


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

    for d, a, b in edges:
        if univ[a - 1] == univ[b - 1]:
            continue
        if find(parent, a) == find(parent, b):
            continue
        answer += d
        union(parent, a, b)

    for i in range(1, n + 1):
        find(parent, i)
        if parent[i] != parent[1]:
            answer = -1
            break

    print(answer)


kruskal()
