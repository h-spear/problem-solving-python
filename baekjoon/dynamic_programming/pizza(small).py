# https://www.acmicpc.net/problem/14606

n = int(input())
dp = [0] * 11
dp[1] = 0
dp[2] = 1
for i in range(3, 11):
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j] + j * (i - j))

print(dp[n])
