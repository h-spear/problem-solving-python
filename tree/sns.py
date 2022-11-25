# https://www.acmicpc.net/problem/2533

import sys


sys.setrecursionlimit(1234567)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


dp = [[0] * 2 for _ in range(n + 1)]
visited = [0] * (n + 1)


def dfs(x):
    global visited
    visited[x] = 1

    dp[x][0] = 0
    dp[x][1] = 1
    for y in graph[x]:
        if visited[y]:
            continue
        dfs(y)
        dp[x][0] += dp[y][1]
        dp[x][1] += min(dp[y])


dfs(1)
print(min(dp[1]))
