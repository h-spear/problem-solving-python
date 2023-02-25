# https://www.acmicpc.net/problem/21736

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

i_x, i_y = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            i_x, i_y = i, j

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque([(i_x, i_y)])
visited = [[False] * m for _ in range(n)]
visited[i_x][i_y] = True
count = 0
while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if not visited[nx][ny] and graph[nx][ny] != "X":
                visited[nx][ny] = True
                q.append((nx, ny))
                if graph[nx][ny] == "P":
                    count += 1

print("TT" if count == 0 else count)
