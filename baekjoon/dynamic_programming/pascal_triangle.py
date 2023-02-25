# https://www.acmicpc.net/problem/16395

dp = [[0] * 31 for _ in range(31)]
n, k = map(int, input().split())

for i in range(1, n + 1):
    dp[i][1] = 1
    dp[i][i] = 1

for i in range(3, n + 1):
    for j in range(2, i + 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

print(dp[n][k])
