# https://www.acmicpc.net/problem/2225

dp = [[0] * 201 for _ in range(201)]
n, k = map(int, input().split())

for i in range(n):
    dp[0][i] = 1
for i in range(k):
    dp[i][0] = i + 1

for i in range(1, k):
    for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[k - 1][n - 1] % 1000000000)
