# https://www.acmicpc.net/problem/1743

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
trash = []
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    trash.append((x - 1, y - 1))

visited = [[0] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    count = 1
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    count += 1

    return count


answer = 0
for x, y in trash:
    answer = max(answer, bfs(x, y))

print(answer)
