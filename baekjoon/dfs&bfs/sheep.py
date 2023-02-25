# https://www.acmicpc.net/problem/3184

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))

wolf = 0
sheep = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == "v":
            wolf += 1
        elif graph[i][j] == "o":
            sheep += 1

visited = [[0] * c for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global wolf, sheep
    q = deque([(x, y)])
    visited[x][y] = 1
    wolf_cnt = 0
    sheep_cnt = 0
    while q:
        x, y = q.popleft()

        if graph[x][y] == "o":
            sheep_cnt += 1
        elif graph[x][y] == "v":
            wolf_cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                if visited[nx][ny] == 0 and graph[nx][ny] != "#":
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    if sheep_cnt > wolf_cnt:
        wolf -= wolf_cnt
    else:
        sheep -= sheep_cnt


for i in range(r):
    for j in range(c):
        if visited[i][j] == 0 and graph[i][j] != "#":
            bfs(i, j)

print(sheep, wolf)
