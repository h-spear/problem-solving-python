# https://www.acmicpc.net/problem/18243

n, k = map(int, input().split())
INF = float("inf")
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def floyd_warshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    graph[i][j] = 0
                    continue
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def is_small_world():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > 6:
                return False
            if graph[i][j] == INF:
                return False
    return True


def solve():
    floyd_warshall()
    if is_small_world():
        print("Small World!")
    else:
        print("Big World!")


solve()
