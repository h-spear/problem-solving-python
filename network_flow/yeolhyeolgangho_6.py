# https://www.acmicpc.net/problem/11409

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

INF = float("inf")
n, m = map(int, input().split())
l = n + m + 1
cost = [[0] * (l + 1) for _ in range(l + 1)]
flow = [[0] * (l + 1) for _ in range(l + 1)]
capacity = [[0] * (l + 1) for _ in range(l + 1)]
start = 0
end = n + m + 1
graph = [[] for _ in range(l + 1)]

for i in range(1, n + 1):
    graph[start].append(i)
    graph[i].append(start)
    capacity[start][i] = 1

for i in range(1, n + 1):
    info = list(map(int, input().split()))
    for k in range(1, len(info), 2):
        j = n + info[k]
        c = info[k + 1]
        graph[i].append(j)
        graph[j].append(i)
        capacity[i][j] = 1
        cost[i][j] += c
        cost[j][i] -= c

for i in range(n + 1, n + m + 1):
    graph[i].append(end)
    graph[end].append(i)
    capacity[i][end] = 1

total_cost = 0
total_flow = 0
while 1:
    q = deque([start])
    visit = [-1] * (n + m + 2)
    distance = [-INF] * (n + m + 2)
    on = [0] * (n + m + 2)
    on[start] = 1
    distance[start] = 0
    while q:
        x = q.popleft()
        on[x] = 0

        for y in graph[x]:
            if (
                capacity[x][y] - flow[x][y] > 0
                and distance[y] < distance[x] + cost[x][y]
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

print(total_flow)
print(total_cost)
