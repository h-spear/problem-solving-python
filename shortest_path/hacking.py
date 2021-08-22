# https://www.acmicpc.net/problem/10282

import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

for tc in range(int(input())):
    v, e, c = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    distance = [INF] * (v + 1)

    def dijkstra(start):
        heap = []
        heapq.heappush(heap, (0, start))
        distance[start] = 0

        while heap:
            dist, now = heapq.heappop(heap)

            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(heap, (cost, i[0]))

    dijkstra(c)

    time, cnt = 0, 0
    for x in distance:
        if x != INF:
            time = max(time, x)
            cnt += 1

    print(cnt, time)
