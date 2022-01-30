# https://www.acmicpc.net/problem/13565

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

m, n = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(y):
    if visited[0][y]:
        return

    q = deque([(0, y)])
    visited[0][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny))


def check_flows():
    for y in range(n):
        if visited[m - 1][y] == 1:
            return "YES"
    return "NO"


for y in range(n):
    if graph[0][y] == 0:
        bfs(y)
print(check_flows())
