# https://www.acmicpc.net/problem/1890

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        jump = graph[i][j]

        if i == j == n - 1:
            break

        if i + jump < n:
            dp[i + jump][j] += dp[i][j]
        if j + jump < n:
            dp[i][j + jump] += dp[i][j]

print(dp[n - 1][n - 1])
