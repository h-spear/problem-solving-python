# https://www.acmicpc.net/problem/1238

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    distance = [INF] * (n + 1)
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    return distance


X_to_house = dijkstra(x)
dist = []
for i in range(1, n + 1):
    house_to_all = dijkstra(i)
    dist.append(house_to_all[x] + X_to_house[i])

print(max(dist))
