# https://www.acmicpc.net/problem/1600

import sys, heapq

input = lambda: sys.stdin.readline().rstrip()

k = int(input())
w, h = map(int, input().split())
graph = []
for _ in range(h):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dx_h = [2, 2, -2, -2, 1, -1, 1, -1]
dy_h = [1, -1, 1, -1, 2, 2, -2, -2]


def bfs():
    q = []
    visited = [[[False] * w for _ in range(h)] for _ in range(32)]
    heapq.heappush(q, (0, k, 0, 0))
    while q:
        cnt, horse, x, y = heapq.heappop(q)

        if x == h - 1 and y == w - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                if visited[horse + 1][nx][ny] == False and graph[nx][ny] != 1:
                    visited[horse + 1][nx][ny] = True
                    heapq.heappush(q, (cnt + 1, horse, nx, ny))

        if horse:
            for i in range(8):
                nx = x + dx_h[i]
                ny = y + dy_h[i]

                if nx >= 0 and nx < h and ny >= 0 and ny < w:
                    if visited[horse][nx][ny] == False and graph[nx][ny] != 1:
                        visited[horse][nx][ny] = True
                        heapq.heappush(q, (cnt + 1, horse - 1, nx, ny))
    return -1


print(bfs())
