# https://www.acmicpc.net/problem/2665

import heapq

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dijkstra(x, y):
    heap = []
    heapq.heappush(heap, (0, (x, y)))
    visited = [[False] * n for _ in range(n)]

    while heap:
        cnt, now = heapq.heappop(heap)
        x, y = now

        if x == y == n - 1:
            print(cnt)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    if graph[nx][ny] == 0:
                        heapq.heappush(heap, (cnt + 1, (nx, ny)))
                    else:
                        heapq.heappush(heap, (cnt, (nx, ny)))


dijkstra(0, 0)
