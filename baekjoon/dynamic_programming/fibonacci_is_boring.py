# https://www.acmicpc.net/problem/17175

p = 1000000007
n = int(input())
dp = [0] * 51
dp[0] = 1
dp[1] = 1
dp[2] = 3
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + 1) % p


print(dp[n])
