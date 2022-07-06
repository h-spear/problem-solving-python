# https://www.acmicpc.net/problem/1652

import re

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))

rotated = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated[i][j] = graph[j][i]


w, h = 0, 0
for r in graph:
    r = "".join(r)
    f = re.findall("(\.){2,}", r)
    w += len(f)


for r in rotated:
    r = "".join(r)
    f = re.findall("(\.){2,}", r)
    h += len(f)

print(w, h)
