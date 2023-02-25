# https://www.acmicpc.net/problem/16469

import sys
from collections import deque

INF = float("inf")
input = lambda: sys.stdin.readline().rstrip()
r, c = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(r)]
enemy = [list(map(int, input().split())) for _ in range(3)]
total_vis = [[0] * c for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[0] * c for _ in range(r)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    for i in range(r):
        for j in range(c):
            if visited[i][j] == 0:
                total_vis[i][j] = INF
            else:
                total_vis[i][j] = max(total_vis[i][j], visited[i][j] - 1)


for a, b in enemy:
    bfs(a - 1, b - 1)

answer = INF
cnt = 0
for i in range(r):
    for j in range(c):
        if total_vis[i][j] == answer:
            cnt += 1
        elif total_vis[i][j] < answer:
            answer = min(answer, total_vis[i][j])
            cnt = 1

if answer == INF:
    print(-1)
else:
    print(answer)
    print(cnt)
