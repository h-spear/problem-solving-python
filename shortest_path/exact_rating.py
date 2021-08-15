import sys

INF = int(1e9)
v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]

for a in range(1, v + 1):
    for b in range(1, v + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(e):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1

# floyd warshall
for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for r in range(1, v + 1):
    count = 0
    for c in range(1, v + 1):
        if graph[r][c] != INF or graph[c][r] != INF:
            count += 1

    if count == v:
        result += 1

print(result)
