# https://www.acmicpc.net/problem/1753

import heapq
import sys

INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((v, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for x in distance[1:]:
    print("INF" if x == INF else x)
