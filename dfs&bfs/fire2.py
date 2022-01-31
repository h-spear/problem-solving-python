# https://www.acmicpc.net/problem/5427

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def get_info(graph, h, w):
    fire = deque()
    x, y = 0, 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "*":
                fire.append((i, j, 0))
            if graph[i][j] == "@":
                x, y = i, j
                graph[i][j] = "."
    return x, y, fire


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph, h, w):
    x, y, fire = get_info(graph, h, w)
    q = deque([(x, y, 0)])
    visited = [[0] * w for _ in range(h)]
    visited[x][y] = 1
    while q:
        x, y, t = q.popleft()

        if x == 0 or y == 0 or x == h - 1 or y == w - 1:
            print(t + 1)
            return

        # fire spreads
        while fire and fire[0][2] == t:
            f_x, f_y, f_t = fire.popleft()
            for i in range(4):
                nfx = f_x + dx[i]
                nfy = f_y + dy[i]
                if nfx < 0 or nfy < 0 or nfx >= h or nfy >= w:
                    continue
                if graph[nfx][nfy] == "#":
                    continue
                if graph[nfx][nfy] == "*":
                    continue
                graph[nfx][nfy] = "*"
                fire.append((nfx, nfy, f_t + 1))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == "#":
                continue
            if graph[nx][ny] == "*":
                continue
            visited[nx][ny] = 1
            q.append((nx, ny, t + 1))

    print("IMPOSSIBLE")


for tc in range(int(input())):
    w, h = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    bfs(graph, h, w)
