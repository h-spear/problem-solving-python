# https://www.acmicpc.net/problem/9372


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


for tc in range(int(input())):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))

    cnt = 0
    for a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        cnt += 1
        union(parent, a, b)

    print(cnt)
