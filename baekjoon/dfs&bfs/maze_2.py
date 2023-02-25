# https://www.acmicpc.net/problem/2178

from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    data = list(map(int, list(input())))
    graph.append(data)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    visited = []
    q = deque([(1, x, y)])
    visited.append((x, y))

    while q:
        cost, x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return cost

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in visited:
                if graph[nx][ny] != 0:
                    q.append((cost + 1, nx, ny))
                    visited.append((nx, ny))


print(bfs(0, 0))
