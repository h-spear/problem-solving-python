# https://www.acmicpc.net/problem/1303

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * n for _ in range(m)]
team = dict()
team["W"], team["B"] = 0, 0


def bfs(x, y):
    visited[x][y] = True
    q = deque([(x, y)])
    color = graph[x][y]
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if not visited[nx][ny] and graph[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1

    team[color] += cnt ** 2


for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)

print(team["W"], team["B"])
