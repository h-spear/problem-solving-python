# https://www.acmicpc.net/problem/1726

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
s_x, s_y, s_dir = map(int, input().split())
e_x, e_y, e_dir = map(int, input().split())
s_x, s_y, s_dir, e_x, e_y, e_dir = (
    s_x - 1,
    s_y - 1,
    s_dir - 1,
    e_x - 1,
    e_y - 1,
    e_dir - 1,
)

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    q = deque([(s_x, s_y, s_dir)])
    visited = [[[0] * 4 for _ in range(n)] for _ in range(m)]
    visited[s_x][s_y][s_dir] = 1
    while q:
        x, y, dir = q.popleft()

        if x == e_x and y == e_y and dir == e_dir:
            print(visited[x][y][dir] - 1)
            return

        # Turn
        nd = [2, 3] if dir < 2 else [0, 1]
        for d in nd:
            if visited[x][y][d]:
                continue
            q.append((x, y, d))
            visited[x][y][d] = visited[x][y][dir] + 1

        # Go
        nx, ny = x, y
        for _ in range(3):
            nx = nx + dx[dir]
            ny = ny + dy[dir]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visited[nx][ny][dir]:
                continue
            if graph[nx][ny] == 1:
                break
            q.append((nx, ny, dir))
            visited[nx][ny][dir] = visited[x][y][dir] + 1
    return


bfs()
