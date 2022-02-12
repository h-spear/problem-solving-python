# https://www.acmicpc.net/problem/1613

INF = float("inf")
n, k = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]


def graph_init():
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1


def floyd_warshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1


def solve():
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())

        if graph[a][b] == 1:
            print(-1)
        elif graph[b][a] == 1:
            print(1)
        else:
            print(0)


graph_init()
floyd_warshall()
solve()
