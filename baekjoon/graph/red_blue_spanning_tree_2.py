# https://www.acmicpc.net/problem/16950


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


def kruskal(color):
    parent = [i for i in range(n + 1)]
    boolean = False if color else True
    edges.sort(reverse=boolean)
    used = []
    cnt = 0
    blue = 0
    for c, f, t in edges:
        if find(parent, f) == find(parent, t):
            continue

        union(parent, f, t)
        cnt += 1
        if c == color:
            used.append((f, t))
        if c == 1:
            blue += 1
    if cnt != n - 1:
        return -1, None
    return blue, used


n, m, k = map(int, input().split())
parent = []
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

result = []
blue_max, red_component = kruskal(0)
blue_min, blue_component = kruskal(1)
result.extend(red_component)
result.extend(blue_component)

if blue_min > k or blue_max < k or red_component == None or blue_component == None:
    print(0)
else:
    parent = [i for i in range(n + 1)]
    for f, t in result:
        union(parent, f, t)

    cnt = len(blue_component)
    edges.sort(reverse=True)
    for c, f, t in edges:
        if find(parent, f) == find(parent, t):
            continue
        if c == 1:
            if cnt == k:
                continue
            cnt += 1
        union(parent, f, t)
        result.append((f, t))

    for x in result:
        print(*x)
