# https://www.acmicpc.net/problem/4792


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
    blue = 0
    cnt = 0
    for c, f, t in edges:
        if find(parent, f) == find(parent, t):
            continue

        union(parent, f, t)
        cnt += 1
        if c:
            blue += 1
    if cnt != n - 1:
        return -1
    return blue


while 1:
    n, m, k = map(int, input().split())
    if n == m == k == 0:
        break

    edges = []
    for _ in range(m):
        c, f, t = input().split()
        if c == "B":
            c = 1
        else:
            c = 0

        f = int(f)
        t = int(t)
        edges.append((c, f, t))

    parent = [i for i in range(n + 1)]
    edges.sort()
    blue_min = kruskal()

    parent = [i for i in range(n + 1)]
    edges.sort(reverse=True)
    blue_max = kruskal()

    if blue_max < k or k < blue_min or blue_max == -1 or blue_min == -1:
        print(0)
    else:
        print(1)
