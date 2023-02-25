# https://www.acmicpc.net/problem/11408

from collections import defaultdict, deque


INF = float("inf")
n, m = map(int, input().split())
node_count = n + m + 1
capacity = [[0] * (node_count + 1) for _ in range(node_count + 1)]
flow = [[0] * (node_count + 1) for _ in range(node_count + 1)]
cost = [[0] * (node_count + 1) for _ in range(node_count + 1)]
graph = defaultdict(list)
start = 0
end = n + m + 1

for i in range(1, n + 1):
    graph[start].append(i)
    graph[i].append(start)
    capacity[start][i] = 1

for i in range(1, n + 1):
    info = list(map(int, input().split()))
    for k in range(1, len(info), 2):
        j = info[k] + n
        graph[i].append(j)
        graph[j].append(i)
        capacity[i][j] = 1
        cost[i][j] = info[k + 1]
        cost[j][i] = -info[k + 1]

for i in range(n + 1, n + m + 1):
    graph[i].append(end)
    graph[end].append(i)
    capacity[i][end] = 1

total_flow = 0
total_cost = 0
while 1:
    visit = [-1] * (node_count + 1)
    q = deque([start])
    distance = [INF] * (node_count + 1)
    distance[start] = 0
    on = [0] * (node_count + 1)
    on[start] = 1
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

print(total_flow)
print(total_cost)
