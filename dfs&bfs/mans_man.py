# https://www.acmicpc.net/problem/17267
# 플래티넘 V
# 위 아래로 이동할 때 한 번에 큐에 넣어야 모든 경로를 다 방문하게 됨

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
left, right = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            sx, sy = i, j
            graph[i][j] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque([(left, right, sx, sy)])
    visited = [[0] * m for _ in range(n)]
    visited[sx][sy] = 1
    while q:
        l, r, x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue
            if i == 2 and r > 0:
                q.append((l, r - 1, nx, ny))
                visited[nx][ny] = 1
            elif i == 3 and l > 0:
                q.append((l - 1, r, nx, ny))
                visited[nx][ny] = 1
            elif i < 2:
                while 1:
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        break
                    if graph[nx][ny] == 1:
                        break
                    visited[nx][ny] = 1
                    q.append((l, r, nx, ny))
                    nx += dx[i]
                    ny += dy[i]

    answer = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                answer += 1
    print(answer)


bfs()
