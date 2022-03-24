# https://www.acmicpc.net/problem/17271

n, m = map(int, input().split())
dp = [0] * 10001
dp[1] = 1
dp[m] = 1
p = 1000000007
for i in range(2, n + 1):
    dp[i] += dp[i - 1]
    if i - m >= 0:
        dp[i] += dp[i - m]
    dp[i] %= p

print(dp[n])
