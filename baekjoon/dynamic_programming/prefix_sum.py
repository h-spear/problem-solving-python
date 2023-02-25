# https://www.acmicpc.net/problem/11660

import sys, numpy

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[0] * (n + 1)]
dp = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(n):
    input_data = list(map(int, input().rstrip().split()))
    input_data.insert(0, 0)
    graph.append(input_data)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + graph[i][j] - dp[i - 1][j - 1]

for _ in range(m):
    x_1, y_1, x_2, y_2 = map(int, input().rstrip().split())
    print(dp[x_2][y_2] - dp[x_2][y_1 - 1] - dp[x_1 - 1][y_2] + dp[x_1 - 1][y_1 - 1])
