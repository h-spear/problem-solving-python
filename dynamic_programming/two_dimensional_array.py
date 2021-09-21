# https://www.acmicpc.net/problem/2167

graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

sum_graph = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_graph[i][j] = sum_graph[i][j - 1] + graph[i - 1][j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_graph[i][j] += sum_graph[i - 1][j]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(
        sum_graph[x][y]
        - sum_graph[i - 1][y]
        - sum_graph[x][j - 1]
        + sum_graph[i - 1][j - 1]
    )
gs
