# https://www.acmicpc.net/problem/2316
# 정점 분할

from collections import deque


def edmonds_karp(start, end):
    total_flow = 0
    while 1:
        visit = [-1] * (2 * N + 1)
        q = deque()
        q.append(start)
        while q:
            x = q.popleft()

            if x == end:
                break

            for y in graph[x]:
                if capacity[x][y] - flow[x][y] > 0 and visit[y] == -1:
                    q.append(y)
                    visit[y] = x

        if visit[end] == -1:
            break

        min_flow = 1

        i = end
        while i != start:
            flow[visit[i]][i] += min_flow
            flow[i][visit[i]] -= min_flow
            i = visit[i]
        total_flow += min_flow

    return total_flow


N = 400
INF = float("inf")
n, p = map(int, input().split())
graph = [[] for _ in range(2 * N + 1)]
capacity = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
flow = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]

for i in range(1, n + 1):
    graph[i].append(i + N)
    graph[i + N].append(i)
    capacity[i][i + N] = 1


for _ in range(p):
    a, b = map(int, input().split())
    graph[a + N].append(b)
    graph[b].append(a + N)
    capacity[a + N][b] = 1

    graph[b + N].append(a)
    graph[a].append(b + N)
    capacity[b + N][a] = 1

print(edmonds_karp(N + 1, 2))
