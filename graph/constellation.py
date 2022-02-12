# https://www.acmicpc.net/problem/4386


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


n = int(input())
stars = []
edges = []
parent = [0] * (n + 1)
for _ in range(n):
    stars.append(tuple(map(float, input().split())))

for i in range(1, n + 1):
    parent[i] = i

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        edges.append((dist, i, j))

edges.sort()
answer = 0

for dist, a, b in edges:
    if find(parent, a) == find(parent, b):
        continue
    answer += dist
    union(parent, a, b)

print(answer)
