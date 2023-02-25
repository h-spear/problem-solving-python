import heapq

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = float("inf")
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)

        if dist < distance[now]:
            continue

        for next, d in graph[now]:
            cost = dist + d
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(heap, (cost, next))

    longest = max(distance[1:])
    print(longest * 2)


dijkstra(k)
