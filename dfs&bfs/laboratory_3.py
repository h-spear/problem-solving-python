# https://www.acmicpc.net/problem/17142

import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
labor = []
for _ in range(n):
    labor.append(list(map(int, input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def virus():
    pos = []
    for i in range(n):
        for j in range(n):
            if labor[i][j] == 2:
                pos.append((i, j))
    return pos


def isCompleted(visited, graph):
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] == 0:
                return False
    return True


def bfs(virus):
    graph = deepcopy(labor)
    visited = [[-1] * n for _ in range(n)]
    for x, y in virus:
        graph[x][y] = 3
        visited[x][y] = 0
    q = deque(virus)
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:

                if (visited[nx][ny] == -1 and graph[nx][ny] == 0) or (
                    visited[nx][ny] == -1
                    and graph[nx][ny] == 2
                    and isCompleted(visited, graph) == False
                ):
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    MAX = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] == 0:
                return int(1e9)
            if visited[i][j] != -1:
                MAX = max(MAX, visited[i][j])

    return MAX


answer = int(1e9)
for candidate in combinations(virus(), m):
    answer = min(answer, bfs(candidate))

print(-1 if answer == int(1e9) else answer)
