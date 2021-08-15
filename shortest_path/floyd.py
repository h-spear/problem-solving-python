# https://www.acmicpc.net/problem/11404
import sys

INF = int(1e9)

v = int(input())
e = int(input())
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for i in range(1, v + 1):
    graph[i][i] = 0

for _ in range(e):
    start, end, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[start][end] = min(graph[start][end], cost)


def floyd_warshall():
    for k in range(1, v + 1):
        for a in range(1, v + 1):
            for b in range(1, v + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


floyd_warshall()

for i in range(1, v + 1):
    for j in range(1, v + 1):
        print(graph[i][j] if graph[i][j] != INF else 0, end=" ")
    print()
