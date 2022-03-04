# https://www.acmicpc.net/problem/9625

n = int(input())
dp = [[0] * 2 for _ in range(46)]
dp[0][0] = 1
dp[1][1] = 1
for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = sum(dp[i - 1])

print(*dp[n])
