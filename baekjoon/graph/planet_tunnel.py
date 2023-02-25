# https://www.acmicpc.net/problem/2887

import sys


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

parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i


x = []
y = []
z = []

for i in range(n):
    input_data = list(map(int, sys.stdin.readline().rstrip().split()))
    x.append((input_data[0], i))
    y.append((input_data[1], i))
    z.append((input_data[2], i))

x.sort()
y.sort()
z.sort()

edges = []

for i in range(n - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()

# kruskal
result = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)
