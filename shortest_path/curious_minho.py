# https://www.acmicpc.net/problem/1507

n = int(input())
graph = []
check = [[1] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))


def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i == k or j == k:
                    continue
                if graph[i][k] + graph[k][j] == graph[i][j]:
                    check[i][j] = 0
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    print(-1)
                    return

    answer = 0
    for i in range(n):
        for j in range(i + 1, n):
            if check[i][j] == 1:
                answer += graph[i][j]
    print(answer)


floyd_warshall()
