import sys
import heapq

INF = int(1e9)

t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n):
        input_data = list(map(int, sys.stdin.readline().rstrip().split()))
        graph.append(input_data)

    distance = [[INF] * n for _ in range(n)]

    heap = []
    distance[0][0] = graph[0][0]
    heapq.heappush(heap, (distance[0][0], (0, 0)))
    while heap:
        dist, x, y = heapq.heappop(heap)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(heap, (cost, (nx, ny)))
    print(distance[n - 1][n - 1])
