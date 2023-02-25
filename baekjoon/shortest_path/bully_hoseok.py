# https://www.acmicpc.net/problem/20168
# https://www.acmicpc.net/problem/20182
# https://www.acmicpc.net/problem/20183

import sys, heapq
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
n, m, a, b, c = map(int, input().split())
graph = defaultdict(list)
INF = float("inf")
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))
shame_distance = [INF] * (n + 1)

heap = [(0, 0, a)]
shame_distance[a] = 0
while heap:
    shame, dist, now = heapq.heappop(heap)

    if shame > shame_distance[now]:
        continue

    for next, d in graph[now]:
        s = max(shame, d)
        cost = dist + d
        if cost > c:
            continue
        if s < shame_distance[next]:
            shame_distance[next] = s
            heapq.heappush(heap, (s, cost, next))


print(-1 if shame_distance[b] == INF else shame_distance[b])
