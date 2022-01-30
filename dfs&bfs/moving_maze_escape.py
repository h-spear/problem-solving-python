# https://www.acmicpc.net/problem/16954

from copy import deepcopy
from collections import deque

graph = []
graph.append([list(input()) for _ in range(8)])

for i in range(8):
    copied = deepcopy(graph[i])
    copied.pop()
    copied.insert(0, ["."] * 8)
    graph.append(copied)

dx = [-1, -1, 0, 1, 1, 1, 0, -1, 0]
dy = [0, 1, 1, 1, 0, -1, -1, -1, 0]


def bfs(x, y):
    global target_x, target_y
    q = deque([(x, y, 0)])

    while q:
        x, y, t = q.popleft()

        if t == 7 or (x == target_x and y == target_y):
            return 1

        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                continue
            if graph[t][nx][ny] == "#":
                continue
            if graph[t + 1][nx][ny] == "#":
                continue
            q.append((nx, ny, t + 1))
    return 0


target_x, target_y = 0, 7
print(bfs(7, 0))
