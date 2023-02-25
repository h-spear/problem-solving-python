# https://www.acmicpc.net/problem/16988

from collections import deque
from itertools import combinations
from copy import deepcopy

graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0] * m for _ in range(n)]
cluster = []
scores = []
candidates = []


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    score = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny] == 0 and graph[nx][ny] == 2:
                visited[nx][ny] = 1
                q.append((nx, ny))
                score += 1
    return score


def clustering():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                candidates.append((i, j))
            if visited[i][j] == 0 and graph[i][j] == 2:
                cluster.append((i, j))
                scores.append(bfs(i, j))


def bfs2(graph, _i, x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    cnt = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                return 0

            if visited[nx][ny] == 0 and graph[nx][ny] == 2:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return scores[_i]


def simul(graph):
    global answer
    now = 0
    for i, c in enumerate(cluster):
        x, y = c
        now += bfs2(graph, i, x, y)
    answer = max(answer, now)


answer = 0
clustering()

for candidate in combinations(candidates, 2):
    pos1, pos2 = candidate
    x1, y1 = pos1
    x2, y2 = pos2

    visited = [[0] * m for _ in range(n)]
    graph_copy = deepcopy(graph)
    graph_copy[x1][y1] = 1
    graph_copy[x2][y2] = 1
    simul(graph_copy)

print(answer)
