# https://www.acmicpc.net/problem/2133

n = int(input())
dp = [0] * (n + 5)
dp[0] = 1
dp[2] = 3
for i in range(3, n + 1):
    if i & 1:
        continue
    else:
        dp[i] = dp[i - 2] * 3
        for j in range(0, i - 2, 2):
            dp[i] += dp[j] * 2

print(dp[n])
