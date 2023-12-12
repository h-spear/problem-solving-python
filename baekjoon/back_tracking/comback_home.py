# https://www.acmicpc.net/problem/1189

import sys

input = lambda: sys.stdin.readline().rstrip()

R, C, K = map(int, input().split())
graph = [[0] * C for _ in range(R)]

for i in range(R):
    line = input()
    for j in range(C):
        if line[j] == "T":
            graph[i][j] = 1

visited = [[0] * C for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, depth):
    global answer

    if depth == K - 1:
        if x == 0 and y == C - 1:
            return 1
        return 0

    visited[x][y] = 1

    temp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        if visited[nx][ny]:
            continue
        if graph[nx][ny] == 1:
            continue
        temp += dfs(nx, ny, depth + 1)

    visited[x][y] = 0
    return temp


print(dfs(R - 1, 0, 0))
