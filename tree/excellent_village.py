# https://www.acmicpc.net/problem/1949

import sys

sys.setrecursionlimit(12345)


def dfs(x):
    visited[x] = 1
    dp[x][0] = 0
    dp[x][1] = citizen[x]
    for y in graph[x]:
        if visited[y]:
            continue
        dfs(y)
        dp[x][0] += max(dp[y])
        dp[x][1] += dp[y][0]


input = lambda: sys.stdin.readline().rstrip()
n = int(input())
citizen = list(map(int, input().split()))
citizen.insert(0, 0)
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
dp = [[0] * 2 for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


dfs(1)
print(max(dp[1]))
