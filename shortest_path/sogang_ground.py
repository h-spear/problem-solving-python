# https://www.acmicpc.net/problem/14938

INF = float("inf")
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
    a, b, d = map(int, input().split())
    graph[a][b] = d
    graph[b][a] = d


def floyd_warshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    graph[i][j] = 0
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def solve():
    answer = 0
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if graph[i][j] <= m:
                cnt += items[j - 1]
        answer = max(answer, cnt)
    print(answer)


floyd_warshall()
solve()
