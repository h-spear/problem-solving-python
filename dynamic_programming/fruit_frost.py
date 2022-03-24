n = int(input())
m = int(input())

dp = [[0] * 31 for _ in range(11)]
for j in range(1, m + 1):
    dp[1][j] = 1

for i in range(2, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

print(dp[n][m])
