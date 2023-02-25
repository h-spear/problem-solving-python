# https://www.acmicpc.net/problem/1277

import sys, heapq
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")
n, w = map(int, input().split())
m = float(input())
hash = {i: tuple(map(int, input().split())) for i in range(1, n + 1)}
graph = defaultdict(list)
line = set(tuple(sorted(map(int, input().split()))) for _ in range(w))

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if i == j:
            continue
        x1, y1 = hash[i]
        x2, y2 = hash[j]
        w = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if (i, j) not in line and (w > m):
            continue
        graph[i].append((j, w))
        graph[j].append((i, w))


def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 1))
    distance = [INF] * (n + 1)
    distance[1] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for next, d in graph[now]:
            if tuple(sorted([now, next])) in line:
                d = 0
            cost = dist + d
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(heap, (cost, next))

    print(int(distance[n] * 1000))


dijkstra()
