# https://www.acmicpc.net/problem/2573
# pypy3

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(i, j):
    q = deque([(i, j)])
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] != 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return visited


def isSeparated():
    isBFS = False
    visited = None
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                visited = bfs(i, j)
                isBFS = True
                break
        if isBFS:
            break

    if visited == None:
        print(0)
        exit()

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and graph[i][j] != 0:
                return True
    return False


def melt():
    contacted = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if graph[nx][ny] == 0:
                            contacted[i][j] += 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] <= contacted[i][j]:
                graph[i][j] = 0
            else:
                graph[i][j] -= contacted[i][j]


def simulate():
    cnt = 0
    while not isSeparated():
        melt()
        cnt += 1
    print(cnt)


simulate()
