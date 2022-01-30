# https://www.acmicpc.net/problem/17129

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]


def start_pos():
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 2:
                continue
            return (i, j)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(pos):
    x, y = pos
    q = deque([pos])
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        if graph[x][y] >= 3:
            print("TAK")
            print(visited[x][y] - 1)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            if visited[nx][ny]:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    print("NIE")


bfs(start_pos())
