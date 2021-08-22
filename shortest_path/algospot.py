# https://www.acmicpc.net/problem/1261

import heapq

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, list(input()))))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0] * n for _ in range(m)]


def dijkstra(x, y):
    heap = []
    heapq.heappush(heap, (0, x, y))
    visited[x][y] = 1

    while heap:
        cnt, x, y = heapq.heappop(heap)
        if x == m - 1 and y == n - 1:
            print(cnt)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1

                    if graph[nx][ny] == 1:
                        heapq.heappush(heap, (cnt + 1, nx, ny))
                    else:
                        heapq.heappush(heap, (cnt, nx, ny))


dijkstra(0, 0)
