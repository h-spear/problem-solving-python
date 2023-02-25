# https://www.acmicpc.net/problem/2146

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def numbering_island(x, y, number):
    q = deque([(x, y)])
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        graph[x][y] = number

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


def bfs(x, y, number):
    q = deque([(x, y)])
    visited = [[-1] * n for _ in range(n)]
    visited[x][y] = 0
    while q:
        x, y = q.popleft()

        if graph[x][y] != 0 and graph[x][y] != number:
            return visited[x][y] - 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if visited[nx][ny] == -1 and graph[nx][ny] != number:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return int(1e9)


# numbering
number = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            numbering_island(i, j, number)
            number += 1

answer = int(1e9)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == 0:
                    answer = min(answer, bfs(i, j, graph[i][j]))
                    break

print(answer)
