# https://www.acmicpc.net/problem/17086

import sys
from collections import deque

INF = int(1e9)

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

distance = [[INF] * m for _ in range(n)]


def bfs(x, y):
    visited = [[-1] * m for _ in range(n)]
    q = deque([(x, y)])
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        distance[x][y] = min(distance[x][y], visited[x][y])

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[nx][ny] == -1 and graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

answer = 0
for row in distance:
    answer = max(answer, max(row))

print(answer)
