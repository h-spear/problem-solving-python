# https://www.acmicpc.net/problem/18223

import sys, heapq
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
v, e, p = map(int, input().split())
INF = float("inf")
graph = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [INF] * (v + 1)
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for next, d in graph[now]:
            cost = dist + d
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(heap, (cost, next))
    return distance[end]


if dijkstra(1, v) >= dijkstra(1, p) + dijkstra(p, v):
    print("SAVE HIM")
else:
    print("GOOD BYE")
