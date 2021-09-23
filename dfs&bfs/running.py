# https://www.acmicpc.net/problem/16930

import sys
from collections import deque

INF = int(1e9)

input = lambda: sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

x1, y1, x2, y2 = map(int, input().split())

visited = [[INF] * m for _ in range(n)]
q = deque([(x1 - 1, y1 - 1)])
visited[x1 - 1][y1 - 1] = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

while q:
    x, y = q.popleft()

    if x == x2 - 1 and y == y2 - 1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        cnt = 1
        while (
            cnt <= k
            and nx >= 0
            and nx < n
            and ny >= 0
            and ny < m
            and visited[nx][ny] > visited[x][y]
            and graph[nx][ny] != "#"
        ):
            if visited[nx][ny] == INF:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            nx += dx[i]
            ny += dy[i]
            cnt += 1


print(-1 if visited[x2 - 1][y2 - 1] == INF else visited[x2 - 1][y2 - 1])
