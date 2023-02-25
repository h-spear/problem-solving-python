# https://www.acmicpc.net/problem/4485

import sys, heapq

input = sys.stdin.readline

i = 1
while True:
    n = int(input())

    if n == 0:
        break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def dijkstra(x, y):
        heap = []
        heapq.heappush(heap, (graph[x][y], (x, y)))
        visited = [[False] * n for _ in range(n)]
        while heap:
            lost, now = heapq.heappop(heap)
            x, y = now

            if x == y == n - 1:
                return lost

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if visited[nx][ny] == False:
                        visited[nx][ny] = True
                        heapq.heappush(heap, (lost + graph[nx][ny], (nx, ny)))

    print("Problem ", i, ": ", dijkstra(0, 0), sep="")
    i += 1
