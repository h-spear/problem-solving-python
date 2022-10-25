# https://school.programmers.co.kr/learn/courses/30/lessons/132266

import heapq


def solution(n, roads, sources, destination):
    INF = float("inf")
    heap = []
    answer = []
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    heapq.heappush(heap, (0, destination))
    distance[destination] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for _next in graph[now]:
            cost = dist + 1
            if distance[_next] > cost:
                distance[_next] = cost
                heapq.heappush(heap, (cost, _next))

    for source in sources:
        answer.append(distance[source] if distance[source] != INF else -1)

    return answer
