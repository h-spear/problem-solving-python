# https://www.acmicpc.net/problem/11058

n = int(input())
dp = [0] * (n + 10)
dp[1] = 1

for i in range(1, n + 1):
    dp[i + 1] = max(dp[i + 1], dp[i] + 1)

    for j in range(i + 3, n + 1):
        dp[j] = max(dp[j], (j - i - 1) * dp[i])


print(dp[n])
