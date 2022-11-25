# https://www.acmicpc.net/problem/2213

import sys


sys.setrecursionlimit(12345)


def dfs(x):
    visited[x] = 1

    dp[x][0] = 0
    dp[x][1] = w[x - 1]
    for y in graph[x]:
        if visited[y]:
            continue
        dfs(y)
        dp[x][0] += max(dp[y])
        dp[x][1] += dp[y][0]
        idxs[x][1].append(y)
        if dp[y][0] < dp[y][1]:
            idxs[x][0].append(y)


input = lambda: sys.stdin.readline().rstrip()
n = int(input())
w = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
dp = [[0] * 2 for _ in range(n + 1)]
visited = [0] * (n + 1)
visited_2 = [0] * (n + 1)
idxs = [[[], []] for _ in range(n + 1)]
path = []

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def trace(x, is_include):
    visited_2[x] = 1
    if is_include:
        path.append(x)
        for y in graph[x]:
            if visited_2[y]:
                continue
            trace(y, 0)
    else:
        for y in graph[x]:
            if visited_2[y]:
                continue

            if dp[y][0] < dp[y][1]:
                trace(y, 1)
            else:
                trace(y, 0)


dfs(1)
if dp[1][0] > dp[1][1]:
    trace(1, 0)
else:
    trace(1, 1)

print(max(dp[1]))
print(*sorted(path))
