# https://www.acmicpc.net/problem/1445

import sys, heapq

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def find_start_and_target():
    s_x, s_y, e_x, e_y = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "S":
                s_x, s_y = i, j
            if graph[i][j] == "F":
                e_x, e_y = i, j
    return s_x, s_y, e_x, e_y


def is_adjacent(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == "g":
            return True
    return False


def dijkstra(start_x, start_y, target_x, target_y):
    visited = [[0] * m for _ in range(n)]
    visited[start_x][start_y] = 1
    heap = []
    heapq.heappush(heap, (0, 0, start_x, start_y))
    while heap:
        garb, adj, x, y = heapq.heappop(heap)

        if x == target_x and y == target_y:
            print(
                garb,
                adj - is_adjacent(target_x, target_y),
            )
            return

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
            elif is_adjacent(nx, ny):
                a += 1

            heapq.heappush(heap, (g, a, nx, ny))
            visited[nx][ny] = 1


def solve():
    s_x, s_y, e_x, e_y = find_start_and_target()
    dijkstra(s_x, s_y, e_x, e_y)


solve()
