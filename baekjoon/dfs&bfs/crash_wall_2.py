# https://www.acmicpc.net/problem/14442

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))


def bfs():
    q = deque([(0, 0, k)])
    visited = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0][k] = 1
    while q:
        x, y, crush = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][crush]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[nx][ny][crush] == -1 and graph[nx][ny] == 0:
                    visited[nx][ny][crush] = visited[x][y][crush] + 1
                    q.append((nx, ny, crush))

                if crush >= 1 and graph[nx][ny] == 1:
                    if visited[nx][ny][crush - 1] == -1:
                        visited[nx][ny][crush - 1] = visited[x][y][crush] + 1
                        q.append((nx, ny, crush - 1))
    return -1


print(bfs())
