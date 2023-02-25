# https://www.acmicpc.net/problem/12026

INF = int(1e9)
n = int(input())
block = " "
block += input()
dp = [INF] * (n + 1)
dp[0] = 0
dp[1] = 0
for i in range(1, n + 1):
    for j in range(i):
        if block[i] == "B" and block[j] == "J":
            dp[i] = min(dp[j] + (i - j) ** 2, dp[i])
        if block[i] == "O" and block[j] == "B":
            dp[i] = min(dp[j] + (i - j) ** 2, dp[i])
        if block[i] == "J" and block[j] == "O":
            dp[i] = min(dp[j] + (i - j) ** 2, dp[i])

print(-1 if dp[n] == INF else dp[n])
