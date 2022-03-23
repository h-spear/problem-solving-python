# https://www.acmicpc.net/problem/17212

n = int(input())
INF = int(1e9)
dp = [INF] * 100001
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 1
dp[6] = 2
dp[7] = 1

for i in range(8, n + 1):
    dp[i] = min(dp[i - 1] + 1, dp[i - 2] + 1, dp[i - 5] + 1, dp[i - 7] + 1, dp[i])

print(dp[n])
