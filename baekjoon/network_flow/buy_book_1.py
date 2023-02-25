# https://www.acmicpc.net/problem/11405
# MCMF(Minimum Cost Maximum Flow)

from collections import deque


INF = float("inf")
MAX_VERTEX = 100
cost = [[0] * (2 * MAX_VERTEX + 2) for _ in range(2 * MAX_VERTEX + 2)]
flow = [[0] * (2 * MAX_VERTEX + 2) for _ in range(2 * MAX_VERTEX + 2)]
capacity = [[0] * (2 * MAX_VERTEX + 2) for _ in range(2 * MAX_VERTEX + 2)]
graph = [[] for _ in range(2 * MAX_VERTEX + 2)]
start = 0
end = 2 * MAX_VERTEX + 1
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(m):
    graph[start].append(i + 1)
    graph[i + 1].append(start)
    capacity[start][i + 1] = b[i]

for i in range(n):
    j = MAX_VERTEX + i
    graph[j + 1].append(end)
    graph[end].append(j + 1)
    capacity[j + 1][end] = a[i]

for i in range(1, m + 1):
    for j in range(MAX_VERTEX + 1, MAX_VERTEX + n + 1):
        graph[i].append(j)
        graph[j].append(i)
        capacity[i][j] = INF

for i in range(1, m + 1):
    c = list(map(int, input().split()))
    for k in range(n):
        j = k + MAX_VERTEX + 1
        cost[i][j] += c[k]
        cost[j][i] -= c[k]

# mcmf
total_cost = 0

while 1:
    q = deque([start])
    distance = [INF] * (2 * MAX_VERTEX + 2)
    visit = [-1] * (2 * MAX_VERTEX + 2)
    on = [0] * (2 * MAX_VERTEX + 2)
    on[start] = 1
    distance[start] = 0
    while q:
        x = q.popleft()
        on[x] = 0

        for y in graph[x]:
            _flow = capacity[x][y] - flow[x][y]
            if _flow > 0 and distance[y] > distance[x] + cost[x][y]:
                distance[y] = distance[x] + cost[x][y]
                visit[y] = x
                if not on[y]:
                    q.append(y)
                    on[y] = 1

    if visit[end] == -1:
        break

    min_flow = INF
    i = end
    while i != start:
        min_flow = min(min_flow, capacity[visit[i]][i] - flow[visit[i]][i])
        i = visit[i]

    i = end
    while i != start:
        flow[visit[i]][i] += min_flow
        flow[i][visit[i]] -= min_flow
        total_cost += min_flow * cost[visit[i]][i]
        i = visit[i]

print(total_cost)
