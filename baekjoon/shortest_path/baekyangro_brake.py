# https://www.acmicpc.net/problem/11562

import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
INF = float("inf")
graph = [[INF] * (n + 1) for _ in range(n + 1)]
question = []

for _ in range(m):
    u, v, b = map(int, input().split())
    graph[u][v] = 0
    if b:
        graph[v][u] = 0
    else:
        graph[v][u] = 1


def floyd_warshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    graph[i][j] = 0
                    continue
                if graph[i][k] != INF and graph[k][j] != INF:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        print(graph[a][b])


floyd_warshall()
