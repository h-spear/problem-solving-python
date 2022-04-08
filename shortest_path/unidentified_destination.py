# https://www.acmicpc.net/problem/9370

import sys, heapq
from collections import defaultdict

for tc in range(int(input())):
    input = lambda: sys.stdin.readline().rstrip()
    INF = float("inf")
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    candidates = []

    for _ in range(t):
        candidates.append(int(input()))

    def dijkstra(start):
        distance = [INF] * (n + 1)
        distance[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            dist, now = heapq.heappop(heap)

            if dist > distance[now]:
                continue

            for next, d in graph[now]:
                cost = dist + d
                if cost < distance[next]:
                    distance[next] = cost
                    heapq.heappush(heap, (cost, next))

        return distance

    def simulation():
        distance_s = dijkstra(s)
        distance_g = dijkstra(g)
        distance_h = dijkstra(h)

        answer = []
        for candidate in candidates:
            dist_destination = distance_s[candidate]
            dist = min(
                distance_s[g] + distance_g[h] + distance_h[candidate],
                distance_s[h] + distance_h[g] + distance_g[candidate],
            )
            if dist != INF and dist == dist_destination:
                answer.append(candidate)

        answer.sort()
        print(*answer)

    simulation()
