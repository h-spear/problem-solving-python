# https://www.acmicpc.net/problem/14940

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def find_target():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                return i, j


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if visited[nx][ny] >= 0:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                visited[i][j] = 0

    for row in visited:
        for x in row:
            print(x, end=" ")
        print()


x, y = find_target()
bfs(x, y)
