# https://www.acmicpc.net/problem/1956

import sys

input = lambda: sys.stdin.readline().rstrip()

INF = float("inf")
v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c


def floyd_warshall():
    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def solve():
    answer = INF
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            answer = min(answer, graph[i][j] + graph[j][i])
    print(-1 if answer == INF else a swer)


floyd_warshall()
solve()
