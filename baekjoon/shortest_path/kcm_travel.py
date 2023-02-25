# https://www.acmicpc.net/problem/10217
# dijkstra + DP
# 참고 : https://developmentdiary.tistory.com/401

from collections import defaultdict

for tc in range(int(input())):
    INF = float("inf")
    graph = defaultdict(list)
    n, m, k = map(int, input().split())
    distance = [[INF] * (m + 1) for _ in range(n + 1)]
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))

    def dijkstra(start):
        distance[start][0] = 0

        for cost in range(m + 1):
            for now in range(1, n + 1):
                if distance[now][cost] == INF:
                    continue

                dist = distance[now][cost]
                for next, c, d in graph[now]:
                    if cost + c > m:
                        continue
                    distance[next][cost + c] = min(distance[next][cost + c], dist + d)

    dijkstra(1)
    if min(distance[n]) == INF:
        print("Poor KCM")
    else:
        print(min(distance[n]))
