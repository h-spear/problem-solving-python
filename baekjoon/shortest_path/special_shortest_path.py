# https://www.acmicpc.net/problem/1504

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    distance = [INF] * (v + 1)
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

    return distance


p1, p2 = map(int, input().split())

answer = min(
    dijkstra(1)[p1] + dijkstra(p1)[p2] + dijkstra(p2)[v],
    dijkstra(1)[p2] + dijkstra(p2)[p1] + dijkstra(p1)[v],
)
print(answer if answer < INF else -1)
