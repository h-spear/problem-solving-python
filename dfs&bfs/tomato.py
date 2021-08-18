# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

m, n = map(int, input().split())
graph = []

for i in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(data)

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))


bfs()


def solution():
    maximum = -1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1
            maximum = max(maximum, graph[i][j])
    return maximum - 1


print(solution())
