# https://www.acmicpc.net/problem/14923

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque([(hx - 1, hy - 1, 0)])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[hx - 1][hy - 1][0] = 1
    while q:
        x, y, use_magic = q.popleft()

        if x == ex - 1 and y == ey - 1:
            return visited[x][y][use_magic] - 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                if use_magic:
                    continue
                if not visited[nx][ny][1]:
                    visited[nx][ny][1] = visited[x][y][use_magic] + 1
                    q.append((nx, ny, 1))
            if visited[nx][ny][use_magic]:
                continue

            if graph[nx][ny] == 1:
                continue
            visited[nx][ny][use_magic] = visited[x][y][use_magic] + 1
            q.append((nx, ny, use_magic))
    return -1


print(bfs())
