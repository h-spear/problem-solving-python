# https://www.acmicpc.net/problem/11123

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, graph, visited):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == ".":
                continue
            q.append((nx, ny))
            visited[nx][ny] = 1
    return 1


def count_flock(graph, h, w):
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == ".":
                continue
            if visited[i][j]:
                continue
            cnt += bfs(i, j, graph, visited)
    return cnt


for tc in range(int(input())):
    h, w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    print(count_flock(graph, h, w))
