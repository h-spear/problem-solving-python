# https://www.acmicpc.net/problem/17070

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 0 가로, 1 세로, 2 대각
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1
for i in range(n):
    for j in range(1, n):
        if i == 0 and j == 1:
            continue
        if graph[i][j] == 0:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
            if graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
                dp[i][j][2] = (
                    dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
                )

print(sum(dp[n - 1][n - 1]))
