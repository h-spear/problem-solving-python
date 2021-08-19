# https://www.acmicpc.net/problem/2583

import sys
from collections import deque

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x_1, y_1, x_2, y_2 = map(int, sys.stdin.readline().rstrip().split())
    for y in range(min(y_1, y_2), max(y_1, y_2)):
        for x in range(min(x_1, x_2), max(x_1, x_2)):
            graph[y][x] = 1

visited = [[False] * n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    area = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if graph[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    area += 1
    return area


result = []
for i in range(m):
    for j in range(n):
        if visited[i][j] == False and graph[i][j] == 0:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for x in result:
    print(x, end=" ")
