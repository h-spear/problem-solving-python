# https://blog.goorm.io/hyundaimobis_preliminary/3/
# 2022 현대모비스 알고리즘 경진대회 예선 문제 2

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    score = 0
    while q:
        x, y = q.popleft()

        if graph[x][y] == 0:
            score += 1
        elif graph[x][y] == 2:
            score -= 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny))

    return score


answer = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        if graph[i][j] == 1:
            continue
        answer = max(answer, bfs(i, j))

print(answer)
