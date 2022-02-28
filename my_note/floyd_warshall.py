import sys

input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c


def print_graph(graph):
    n = len(graph)
    for i in range(1, n):
        for j in range(1, n):
            print(graph[i][j], end=" ")
        print()


def floyd_warshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    graph[i][j] = 0
                    continue
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


floyd_warshall()
print_graph(graph)
