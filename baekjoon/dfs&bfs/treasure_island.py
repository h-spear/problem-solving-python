# https://www.acmicpc.net/problem/2589

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

graph = []
land = []
r, c = map(int, input().split())
for _ in range(r):
    graph.append(list(input()))


for i in range(r):
    for j in range(c):
        if graph[i][j] == "L":
            land.append((i, j))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    max_distance = 0
    target_x, target_y = 0, 0
    visited = [[-1] * c for _ in range(r)]
    q = deque([(x, y)])
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                if graph[nx][ny] == "L" and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    max_distance = max(max_distance, visited[nx][ny])
                    target_x, target_y = x, y

    return max_distance, target_x, target_y


answer = 0
checked = [[False] * c for _ in range(r)]
for i, j in land:
    if checked[i][j] == False:
        max_distance, target_x, target_y = bfs(i, j)
        checked[i][j] = True
        checked[target_x][target_y] = True
        answer = max(max_distance, answer)

print(answer)
