import sys
import heapq

INF = int(1e9)
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [INF] * (n + 1)

# dijkstra
heap = []
distance[1] = 0
heapq.heappush(heap, (distance[1], 1))

while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(heap, (cost, i))

largest = max(distance[1:])
print(distance.index(largest), largest, distance.count(largest))
