# https://www.acmicpc.net/problem/3187

from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))

visited = [[0] * c for _ in range(r)]
cluster = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def clustering(x, y):
    global visited, cluster
    q = deque([(x, y)])
    visited[x][y] = cluster
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] != "#":
                q.append((nx, ny))
                visited[nx][ny] = cluster
    cluster += 1


# 클러스터링
for i in range(r):
    for j in range(c):
        if visited[i][j] == 0 and graph[i][j] != "#":
            clustering(i, j)


counter = [[0] * 2 for _ in range(cluster)]
for i in range(r):
    for j in range(c):
        now = visited[i][j]
        if graph[i][j] == "v":
            counter[now][1] += 1
        if graph[i][j] == "k":
            counter[now][0] += 1

sheep = 0
wolf = 0
for x, y in counter:
    if x > y:
        sheep += x
    else:
        wolf += y

print(sheep, wolf)
