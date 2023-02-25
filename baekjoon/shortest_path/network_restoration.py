# https://www.acmicpc.net/problem/2211

import heapq, sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
INF = float("inf")
distance = [INF] * (n + 1)
prev = [0] * (n + 1)


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for next, d in graph[now]:
            cost = dist + d
            if cost < distance[next]:
                distance[next] = cost
                prev[next] = now
                heapq.heappush(heap, (cost, next))

    print(n - 1)
    for i in range(2, n + 1):
        print(i, prev[i])


dijkstra(1)
