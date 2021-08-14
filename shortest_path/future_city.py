INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# floyd warshall
for k in range(n + 1):
    for a in range(n + 1):
        for b in range(n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

x, k = map(int, input().split())

distance = graph[1][k] + graph[k][x]
print(-1 if distance >= INF else distance)
