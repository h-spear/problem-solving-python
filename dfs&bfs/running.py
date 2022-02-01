# https://www.acmicpc.net/problem/16930

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
graph = [list(input()) for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque([(x1 - 1, y1 - 1)])
visited = [[0] * m for _ in range(n)]
visited[x1 - 1][y1 - 1] = 1
while q:
    x, y = q.popleft()

    if x == x2 - 1 and y == y2 - 1:
        print(visited[x][y] - 1)
        exit(0)

    for i in range(4):
        nx = x
        ny = y
        run = 1
        while run <= k:
            nx += dx[i]
            ny += dy[i]
            run += 1

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] != 0 and visited[nx][ny] <= visited[x][y]:
                break
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == "#":
                break
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

print(-1)
