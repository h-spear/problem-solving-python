# https://www.acmicpc.net/problem/14284

import sys, heapq
from collections import defaultdict

INF = float("inf")
input = lambda: sys.stdin.readline().rstrip()
graph = defaultdict(list)
n, m = map(int, input().split())
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
s, t = map(int, input().split())


def dijkstra():
    heap = []
    heapq.heappush(heap, (0, s))
    distance[s] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue
        for next, d in graph[now]:
            cost = dist + d
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(heap, (cost, next))
    print(distance[t])


dijkstra()
