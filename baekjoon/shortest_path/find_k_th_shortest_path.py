# https://www.acmicpc.net/problem/1854

import heapq


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = 987654321
distance = [[INF] * k for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(x=1):
    heap = []
    heapq.heappush(heap, (0, x))
    distance[x][0] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        for next, d in graph[now]:
            cost = dist + d
            if cost < distance[next][k - 1]:
                distance[next][k - 1] = cost
                distance[next].sort()
                heapq.heappush(heap, (cost, next))

    for i in range(1, n + 1):
        if distance[i][k - 1] == INF:
            print(-1)
        else:
            print(distance[i][k - 1])


dijkstra()
