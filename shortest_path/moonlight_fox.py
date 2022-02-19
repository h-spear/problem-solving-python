# https://www.acmicpc.net/problem/16118
# pypy3 시간초과

import sys, heapq
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
graph = defaultdict(list)
INF = float("inf")
distance_fox = [INF] * (n + 1)
distance_wolf = [[INF] * 2 for _ in range(n + 1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, 2 * d))
    graph[b].append((a, 2 * d))


def dijkstra(start):
    distance = distance_fox
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


def dijkstra_wolf(start):
    distance = distance_wolf
    heap = []
    heapq.heappush(heap, (0, 1, start))
    distance[start][1] = 0
    while heap:
        dist, run, now = heapq.heappop(heap)

        if dist > distance[now][run]:
            continue

        for next, d in graph[now]:
            if run:
                cost = dist + d // 2
            else:
                cost = dist + d * 2

            if cost < distance[next][1 - run]:
                distance[next][1 - run] = cost
                heapq.heappush(heap, (cost, 1 - run, next))

    print(distance)


def solve():
    dijkstra(1)
    dijkstra_wolf(1)

    answer = 0
    for i in range(1, n + 1):
        if distance_fox[i] < min(distance_wolf[i]):
            answer += 1

    print(answer)


solve()
