# https://www.acmicpc.net/problem/11779

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, target = map(int, input().split())

distance = [[INF, 0] for _ in range(n + 1)]


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = [0, -1]

    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now][0]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]][0] > cost:
                distance[i[0]][0] = cost
                distance[i[0]][1] = now
                heapq.heappush(heap, (cost, i[0]))
    return distance


dist = dijkstra(start)

print(dist[target][0])  # 최소 비용 출력

route = [target]
while target != start:
    target = dist[target][1]
    route.append(target)

print(len(route))  # 경로에 포함되어있는 도시의 개수
for i in range(len(route) - 1, -1, -1):  # 도시 순서
    print(route[i], end=" ")
