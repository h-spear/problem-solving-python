# https://www.acmicpc.net/problem/24479

import sys

sys.setrecursionlimit(100000)
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
c = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()


def dfs(now):
    global c
    c += 1
    visited[now] = c

    for next in graph[now]:
        if visited[next]:
            continue
        dfs(next)


dfs(r)

for i in range(1, n + 1):
    print(visited[i])
