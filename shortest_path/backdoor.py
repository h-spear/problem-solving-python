# https://www.acmicpc.net/problem/17396

from collections import defaultdict
import sys, heapq

input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")
n, m = map(int, input().split())
A = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))


def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0))
    distance = [INF] * n
    distance[0] = 0
    while heap:
        dist, x = heapq.heappop(heap)

        if dist > distance[x]:
            continue

        for next, d in graph[x]:
            if next != n - 1 and A[next]:
                continue
            cost = dist + d
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(heap, (cost, next))
    print(-1 if distance[n - 1] == INF else distance[n - 1])


dijkstra()
