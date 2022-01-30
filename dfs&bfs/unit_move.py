# https://www.acmicpc.net/problem/2194

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m, a, b, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
s_x, s_y = map(int, input().split())
e_x, e_y = map(int, input().split())
s_x, s_y, e_x, e_y = s_x - 1, s_y - 1, e_x - 1, e_y - 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def is_overlap(x, y):
    for i in range(b):
        if graph[x][y + i] == 1:
            return True
        if graph[x + a - 1][y + i] == 1:
            return True
    for i in range(a):
        if graph[x + i][y] == 1:
            return True
        if graph[x + i][y + b - 1] == 1:
            return True
    return False


def bfs():
    q = deque([(s_x, s_y)])
    visited = [[0] * (m - b + 1) for _ in range(n - a + 1)]
    visited[s_x][s_y] = 1
    while q:
        x, y = q.popleft()
        if x == e_x and y == e_y:
            print(visited[x][y] - 1)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n - a + 1 or ny >= m - b + 1:
                continue
            if visited[nx][ny]:
                continue
            if is_overlap(nx, ny):
                continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
    print(-1)


bfs()
