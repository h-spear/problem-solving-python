import sys, heapq
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")
graph = defaultdict(list)
V, E = map(int, input().split())
start = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


# O(nlogn)
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [INF] * (V + 1)
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

    print(distance)


dijkstra(start)
