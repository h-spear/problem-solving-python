# https://www.acmicpc.net/problem/10026

import sys
from collections import deque

graph = []
n = int(input())

for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return 1


# 적록색약이 아닌 경우
visited = [[False] * n for _ in range(n)]
result = [0, 0]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            result[0] += bfs(i, j)

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            result[1] += bfs(i, j)

for x in result:
    print(x, end=" ")
