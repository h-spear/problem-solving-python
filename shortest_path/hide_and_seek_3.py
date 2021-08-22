# https://www.acmicpc.net/problem/13549

import heapq

INF = int(1e9)

n, k = map(int, input().split())

distance = [INF] * (100001)


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        time, x = heapq.heappop(heap)
        if x == k:
            print(time)
            return

        if x - 1 >= 0 and distance[x - 1] > time + 1:
            distance[x - 1] = time + 1
            heapq.heappush(heap, (time + 1, x - 1))
        if x + 1 <= 100000 and distance[x + 1] > time + 1:
            distance[x + 1] = time + 1
            heapq.heappush(heap, (time + 1, x + 1))
        if 2 * x <= 100000 and distance[2 * x] > time:
            distance[2 * x] = time
            heapq.heappush(heap, (time, 2 * x))


dijkstra(n)
