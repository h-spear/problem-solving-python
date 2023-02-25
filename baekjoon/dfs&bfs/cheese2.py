# https://www.acmicpc.net/problem/2638

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def air():
    visited = [[False] * m for _ in range(n)]
    q = deque([(0, 0)])
    graph[0][0] = 2
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[nx][ny] == False and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    graph[nx][ny] = 2
                    q.append((nx, ny))


def isContacted(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if graph[nx][ny] == 2:
                cnt += 1
    return cnt >= 2


def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    if graph[nx][ny] == 2:
                        q.append((nx, ny))
                    elif graph[nx][ny] == 1 and isContacted(nx, ny):
                        graph[nx][ny] = 3


def melting():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 3:
                graph[i][j] = 0


def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                graph[i][j] = 0
            elif graph[i][j] == 1:
                cnt += 1
    return cnt != 0


answer = 0
while check():
    air()
    bfs()
    melting()
    answer += 1

print(answer)
