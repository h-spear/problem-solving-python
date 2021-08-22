# https://www.acmicpc.net/problem/6087

import heapq, sys

input = sys.stdin.readline
INF = int(1e6)

w, h = map(int, input().split())
graph = []

for _ in range(h):
    graph.append(list(input()))

laser = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == "C":
            laser.append((i, j))

# up left down right
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

distance = [[INF] * w for _ in range(h)]


def dijkstra(x, y, target_x, target_y):
    heap = []
    heapq.heappush(heap, (0, 0, x, y))
    heapq.heappush(heap, (0, 1, x, y))
    heapq.heappush(heap, (0, 2, x, y))
    heapq.heappush(heap, (0, 3, x, y))
    distance[x][y] = 0

    while heap:
        cnt, dir, x, y = heapq.heappop(heap)

        if cnt > distance[x][y]:
            continue

        if x == target_x and y == target_y:
            return cnt

        for i in [0, -1, 1]:
            nx = x + dx[(dir + i) % 4]
            ny = y + dy[(dir + i) % 4]

            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                if graph[nx][ny] != "*":
                    if i == 0:
                        distance[nx][ny] = min(cnt, distance[nx][ny])
                        heapq.heappush(heap, (cnt, dir, nx, ny))
                    else:
                        distance[nx][ny] = min(cnt + 1, distance[nx][ny])
                        heapq.heappush(heap, (cnt + 1, (dir + i) % 4, nx, ny))


print(dijkstra(laser[0][0], laser[0][1], laser[1][0], laser[1][1]))
