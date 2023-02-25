# https://www.acmicpc.net/problem/1445

import sys, heapq

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
garbage = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

s_x, s_y, e_x, e_y = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == "S":
            s_x, s_y = i, j
        if graph[i][j] == "F":
            e_x, e_y = i, j
        if graph[i][j] == "g":
            garbage.append((i, j))

for x, y in garbage:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] != ".":
            continue
        graph[nx][ny] = "a"


def dijkstra():
    visited = [[0] * m for _ in range(n)]
    visited[s_x][s_y] = 1
    heap = []
    heapq.heappush(heap, (0, 0, s_x, s_y))
    while heap:
        garb, adj, x, y = heapq.heappop(heap)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            g, a = garb, adj

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == "g":
                g += 1
            if graph[nx][ny] == "a":
                a += 1
            if nx == e_x and ny == e_y:
                print(g, a)
                return

            heapq.heappush(heap, (g, a, nx, ny))
            visited[nx][ny] = 1


dijkstra()
