# https://www.acmicpc.net/problem/1719

import sys

INF = float("inf")
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
distance = [[INF] * (n + 1) for _ in range(n + 1)]
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = c
    distance[b][a] = c
    graph[a][b] = b
    graph[b][a] = a


def floyd_warshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    graph[i][j] = "-"
                    continue
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

                    graph[i][j] = graph[i][k]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(graph[i][j], end=" ")
        print()


floyd_warshall()
