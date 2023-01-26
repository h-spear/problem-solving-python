import heapq

# https://school.programmers.co.kr/learn/courses/30/lessons/154538

def solution(x, y, n):
    heap = []
    heapq.heappush(heap, (0, x))
    INF = float("inf")
    distance = [INF] * (y + 1)
    distance[x] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if now == y:
            return dist

        if dist > distance[now]:
            continue

        for _next in [now * 2, now * 3, now + n]:
            if _next > y:
                continue

            cost = distance[now] + 1
            if cost < distance[_next]:
                distance[_next] = cost
                heapq.heappush(heap, (dist + 1, _next))

    return -1
