# https://www.acmicpc.net/problem/5719

import heapq

while 1:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    s, e = map(int, input().split())
    graph = [[] for _ in range(n)]
    INF = float("inf")
    distance = [INF] * (n + 1)
    footprint = [[] for _ in range(n)]
    shortest_path = set()
    visited = [0] * (n + 1)
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append([v, p])

    def dijkstra(start):
        heap = []
        heapq.heappush(heap, (0, start))
        distance[start] = 0
        while heap:
            dist, now = heapq.heappop(heap)

            if dist < distance[start]:
                continue

            for next, d in graph[now]:
                cost = dist + d
                if distance[next] == cost:
                    footprint[next].append(now)

                if distance[next] > cost:
                    distance[next] = cost
                    footprint[next] = [now]
                    heapq.heappush(heap, (cost, next))

    def find_path(x):
        if visited[x]:
            return

        visited[x] = 1
        for prev in footprint[x]:
            shortest_path.add((prev, x))
            find_path(prev)

    def dijkstra2(start):
        heap = []
        heapq.heappush(heap, (0, start))
        distance[start] = 0
        while heap:
            dist, now = heapq.heappop(heap)

            if dist < distance[start]:
                continue

            for next, d in graph[now]:
                if (now, next) in shortest_path:
                    continue

                cost = dist + d
                if distance[next] > cost:
                    distance[next] = cost
                    heapq.heappush(heap, (cost, next))

    def nearly_shortest_path(start, end):
        global distance
        dijkstra(start)
        find_path(end)
        distance = [INF] * (n + 1)
        dijkstra2(start)
        print(-1 if distance[end] == INF else distance[end])

    nearly_shortest_path(s, e)
