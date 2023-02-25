# https://www.acmicpc.net/problem/5972

import heapq
from collections import defaultdict

INF = float("inf")
n, m = map(int, input().split())
graph = defaultdict(list)
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for next, d in graph[now]:
            cost = d + dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(heap, (cost, next))
    print(distance[end])


dijkstra(1, n)
