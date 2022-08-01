# https://school.programmers.co.kr/learn/courses/30/lessons/72413

import heapq


def solution(n, s, a, b, fares):
    INF = float("inf")
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    def dijkstra(s):
        distance = [INF] * (n + 1)
        heap = []
        heapq.heappush(heap, (0, s))
        distance[s] = 0
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

    answer = INF
    for mp, mc in enumerate(dijkstra(s)):
        if mp == INF:
            continue

        distance = dijkstra(mp)
        if distance[a] == INF:
            continue
        if distance[b] == INF:
            continue
        answer = min(answer, mc + distance[a] + distance[b])

    return answer
