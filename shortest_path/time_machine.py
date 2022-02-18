# https://www.acmicpc.net/problem/11657

import sys

input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")
n, m = map(int, input().split())
edges = []
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bellman_ford(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            now, next, cost = edges[j]

            if distance[now] != INF and distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost

                if i == n - 1:
                    return True
    return False


negative_cycle = bellman_ford(1)
if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
