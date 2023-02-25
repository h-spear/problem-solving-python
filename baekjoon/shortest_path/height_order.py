# https://www.acmicpc.net/problem/2458

INF = float("inf")
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1


def floyd_warshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1


def solve():
    answer = 0
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if graph[i][j] == 1 or graph[j][i] == 1:
                cnt += 1

        if cnt == n - 1:
            answer += 1
    print(answer)
    return


floyd_warshall()
solve()
