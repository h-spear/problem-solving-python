# https://www.acmicpc.net/problem/2311
# mcmf 2번, 정점 분할

from collections import deque


INF = float("inf")
OUT = 1005
MAX_VERTEX = OUT * 2
capacity = [[0] * (MAX_VERTEX + 1) for _ in range(MAX_VERTEX + 1)]
flow = [[0] * (MAX_VERTEX + 1) for _ in range(MAX_VERTEX + 1)]
cost = [[0] * (MAX_VERTEX + 1) for _ in range(MAX_VERTEX + 1)]
graph = [[] for _ in range(MAX_VERTEX + 1)]
n, m = map(int, input().split())
start = OUT + 1
end = n

for i in range(1, n + 1):
    graph[i].append(OUT + i)
    graph[OUT + i].append(i)
    capacity[i][OUT + i] = INF


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[OUT + a].append(b)
    graph[b].append(OUT + a)
    capacity[OUT + a][b] = 1
    cost[OUT + a][b] = c
    cost[b][OUT + a] = -c

    graph[OUT + b].append(a)
    graph[a].append(OUT + b)
    capacity[OUT + b][a] = 1
    cost[OUT + b][a] = c
    cost[a][OUT + b] = -c


def mcmf():
    total_cost = 0
    total_flow = 0

    for _ in range(2):
        q = deque([start])
        visit = [-1] * (MAX_VERTEX + 1)
        on = [0] * (MAX_VERTEX + 1)
        on[start] = 1
        distance = [INF] * (MAX_VERTEX + 1)
        distance[start] = 0
        while q:
            x = q.popleft()
            on[x] = 0

            for y in graph[x]:
                if (
                    capacity[x][y] - flow[x][y] > 0
                    and distance[y] > distance[x] + cost[x][y]
                ):
                    distance[y] = distance[x] + cost[x][y]
                    visit[y] = x
                    if not on[y]:
                        q.append(y)
                        on[y] = 1

        if visit[end] == -1:
            break

        min_flow = 1

        i = end
        while i != start:
            flow[visit[i]][i] += min_flow
            flow[i][visit[i]] -= min_flow
            total_cost += cost[visit[i]][i]
            i = visit[i]

        total_flow += min_flow

    return total_cost


print(mcmf())
