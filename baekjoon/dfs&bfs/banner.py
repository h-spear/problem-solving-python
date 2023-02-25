# https://www.acmicpc.net/problem/14716

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(m)]

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]


def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return 1


answer = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            answer += bfs(i, j)

print(answer)
