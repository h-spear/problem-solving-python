# https://www.acmicpc.net/problem/17836

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m, t = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    isPossible = False
    shortest_time = float("inf")  # *****************

    while q:
        x, y = q.popleft()

        if graph[x][y] == 2 and (n - x + m - y - 2 + visited[x][y] - 1) <= t:
            isPossible = True
            shortest_time = n - x + m - y - 2 + visited[x][y] - 1
        if x == n - 1 and y == m - 1:
            isPossible = True
            shortest_time = min(shortest_time, visited[x][y] - 1)
            break
        if visited[x][y] - 1 >= t:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    return shortest_time if isPossible else "Fail"


print(bfs(0, 0))
