# https://www.acmicpc.net/submit/15681/52093996

from collections import defaultdict
import sys

sys.setrecursionlimit(110000)
input = lambda: sys.stdin.readline().rstrip()
dp = {}


def dfs(x):
    global visited, dp
    if visited[x]:
        return dp[x]

    visited[x] = 1
    leaf = 1

    for y in graph[x]:
        if visited[y]:
            continue
        leaf += dfs(y)

    dp[x] = leaf
    return dp[x]


graph = defaultdict(list)
n, r, q = map(int, input().split())
visited = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)
for _ in range(q):
    print(dp[int(input())])
