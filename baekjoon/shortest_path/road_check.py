# https://www.acmicpc.net/problem/2307

import sys, heapq
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")
n, m = map(int, input().split())
graph = defaultdict(list)
edges = []
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
    edges.append((a, b))


def dijkstra(x, y):
    heap = []
    heapq.heappush(heap, (0, 1))
    distance = [INF] * (n + 1)
    distance[1] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for next, d in graph[now]:
            if now == x and next == y:
                continue
            if now == y and next == x:
                continue
            cost = dist + d
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(heap, (cost, next))
    return distance[n]


def solve():
    answer = 0
    for x, y in edges:
        escape_time = dijkstra(x, y)
        if escape_time == INF:
            print(-1)
            return
        answer = max(answer, escape_time)

    print(answer - dijkstra(0, 0))


solve()
