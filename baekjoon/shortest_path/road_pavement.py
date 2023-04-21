# https://www.acmicpc.net/problem/1162

import heapq

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

heap = []
heapq.heappush(heap, (0, k, 1))
INF = float("inf")
distance = [[INF] * (k + 1) for _ in range(n + 1)]
distance[1][k] = 0
while heap:
    dist, wrap, now = heapq.heappop(heap)

    if distance[now][wrap] < dist:
        continue
    for _next, _dist in graph[now]:

        if wrap and distance[_next][wrap - 1] > distance[now][wrap]:
            distance[_next][wrap - 1] = distance[now][wrap]
            heapq.heappush(heap, (distance[now][wrap], wrap - 1, _next))

        cost = _dist + distance[now][wrap]
        if distance[_next][wrap] > cost:
            distance[_next][wrap] = cost
            heapq.heappush(heap, (cost, wrap, _next))


print(min(distance[n]))
