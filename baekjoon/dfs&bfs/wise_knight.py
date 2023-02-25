# https://www.acmicpc.net/problem/18404

import sys
from collections import deque, OrderedDict

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
k_x, k_y = map(int, input().split())
opposite = OrderedDict()
for _ in range(m):
    opposite[tuple(map(int, input().split()))] = 0

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs():
    keys = set(opposite.keys())
    q = deque([(k_x - 1, k_y - 1)])
    visited = [[0] * n for _ in range(n)]
    visited[k_x - 1][k_y - 1] = 1
    while q:
        x, y = q.popleft()

        if (x + 1, y + 1) in keys:
            opposite[(x + 1, y + 1)] = visited[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


bfs()
for x in opposite.values():
    print(x, end=" ")
