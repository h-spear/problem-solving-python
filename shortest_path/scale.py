# https://www.acmicpc.net/problem/10159

INF = float("inf")
n = int(input())
m = int(input())
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
    answer = []
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            if graph[i][j] != 1 and graph[j][i] != 1:
                cnt += 1
        answer.append(cnt)

    for x in answer:
        print(x)


floyd_warshall()
solve()
