# https://www.acmicpc.net/problem/2406


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
    global edges, parent
    answer = 0
    edges.sort()
    added = []
    for cost, a, b in edges:
        if a == 1 or b == 1:
            continue
        if find(parent, a) == find(parent, b):
            continue
        answer += cost
        added.append("{} {}".format(a, b))
        union(parent, a, b)

    print(answer, len(added))
    for x in added:
        print(x)


def is_stable(n):
    for i in range(2, n + 1):
        if find(parent, 2) != find(parent, i):
            return False
    return True


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    union(parent, x, y)

edges = []
for i in range(n):
    input_data = list(map(int, input().split()))
    for j in range(i + 1, n):
        edges.append((input_data[j], i + 1, j + 1))

if is_stable(n):
    print(0, 0)
else:
    kruskal()
