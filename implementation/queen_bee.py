# https://www.acmicpc.net/problem/10836

import sys

input = lambda: sys.stdin.readline().rstrip()
m, n = map(int, input().split())
graph = [[1] * m for _ in range(m)]
worm = [0] * (2 * m - 1)

for _ in range(n):
    a, b, c = map(int, input().split())
    for i in range(a, a + b):
        worm[i] += 1
    for i in range(a + b, a + b + c):
        worm[i] += 2

cnt = 0
for i in range(m - 1, -1, -1):
    graph[i][0] += worm[cnt]
    cnt += 1

for j in range(1, m):
    graph[0][j] += worm[cnt]
    cnt += 1

for i in range(1, m):
    for j in range(1, m):
        graph[i][j] = max(graph[i - 1][j], graph[i][j - 1], graph[i - 1][j - 1])

for row in graph:
    print(*row)
