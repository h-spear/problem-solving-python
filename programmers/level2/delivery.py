# https://programmers.co.kr/learn/courses/30/lessons/12978

import heapq
from collections import defaultdict


def solution(N, road, K):
    graph = defaultdict(list)
    INF = float("inf")
    distance = [INF] * (N + 1)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

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
                    heapq.heappush(heap, (cost, next))

    dijkstra(1)
    return sum([1 for x in distance if x <= K])
