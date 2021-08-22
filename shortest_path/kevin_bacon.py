# https://www.acmicpc.net/problem/1389

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * 101 for _ in range(101)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

dist = []
for i in range(1, n + 1):
    sum = 0
    for j in range(1, n + 1):
        sum += graph[i][j]
    dist.append(sum)

print(dist.index(min(dist)) + 1)
