# https://www.acmicpc.net/problem/2748

dp = [0] * 91
dp[1] = 1
n = int(input())

for i in range(n - 1):
    dp[i + 2] = dp[i + 1] + dp[i]

print(dp[n])
