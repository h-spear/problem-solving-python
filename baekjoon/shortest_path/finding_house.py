# https://www.acmicpc.net/problem/13911

import sys, heapq
from collections import defaultdict

INF = float("inf")
input = lambda: sys.stdin.readline().rstrip()
v, e = map(int, input().split())
graph = defaultdict(list)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

m, x = map(int, input().split())
mc_donalds = set(map(int, input().split()))
s, y = map(int, input().split())
starbucks = set(map(int, input().split()))


def dijkstra(pos):
    distance = [INF] * (v + 1)
    heap = []
    for x in pos:
        distance[x] = 0
        heapq.heappush(heap, (0, x))

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


def solve():
    global x, y
    answer = INF
    distance1 = dijkstra(mc_donalds)
    distance2 = dijkstra(starbucks)

    for i in range(1, v + 1):
        if i in mc_donalds:
            continue
        if i in starbucks:
            continue
        if distance1[i] > x:
            continue
        if distance2[i] > y:
            continue
        dist = distance1[i] + distance2[i]
        answer = min(answer, dist)
    print(-1 if answer == INF else answer)


solve()
