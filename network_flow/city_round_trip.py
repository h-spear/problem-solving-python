# https://www.acmicpc.net/problem/17412
# 용량이 1인 network flow

import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()


def edmonds_karp(start, end):
    total_flow = 0

    while 1:
        # bfs로 start -> end 경로
        visit = [-1] * (n + 1)
        q = deque([start])
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

        # 유량 계산
        min_flow = INF
        i = end
        while i != start:
            min_flow = min(min_flow, capacity[visit[i]][i] - flow[visit[i]][i])
            i = visit[i]

        # flow update
        i = end
        while i != start:
            flow[visit[i]][i] += min_flow
            flow[i][visit[i]] -= min_flow
            i = visit[i]

        total_flow += min_flow
    return total_flow


INF = float("inf")
n, p = map(int, input().split())
graph = defaultdict(list)
capacity = [[0] * (n + 1) for _ in range(n + 1)]
flow = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(p):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    capacity[a][b] = 1

print(edmonds_karp(1, 2))
