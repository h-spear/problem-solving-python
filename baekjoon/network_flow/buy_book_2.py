# https://www.acmicpc.net/problem/11406

from collections import deque

INF = float("inf")
n, m = map(int, input().split())
l = n + m + 1
a = list(map(int, input().split()))
b = list(map(int, input().split()))
graph = [[] for _ in range(l + 1)]
flow = [[0] * (l + 1) for _ in range(l + 1)]
capacity = [[0] * (l + 1) for _ in range(l + 1)]
start = 0
end = l

for i in range(1, m + 1):
    graph[start].append(i)
    graph[i].append(start)
    capacity[start][i] = b[i - 1]

for i in range(1, m + 1):
    c = list(map(int, input().split()))
    for k in range(n):
        j = m + k + 1
        graph[i].append(j)
        graph[j].append(i)
        capacity[i][j] = c[k]

for j in range(1, n + 1):
    i = j + m
    graph[i].append(end)
    graph[end].append(i)
    capacity[i][end] = a[j - 1]

total_flow = 0
while 1:
    q = deque([start])
    visit = [-1] * (l + 1)
    on = [0] * (l + 1)
    on[start] = 1
    while q:
        x = q.popleft()
        on[x] = 0

        for y in graph[x]:
            if capacity[x][y] - flow[x][y] > 0 and visit[y] == -1:
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
        i = visit[i]

    total_flow += min_flow

print(total_flow)
