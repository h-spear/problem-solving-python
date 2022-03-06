# https://www.acmicpc.net/problem/16194

n = int(input())
prices = [0]
prices.extend(list(map(int, input().split())))
dp = [1234567] * (n + 1)
dp[1] = prices[1]

for i in range(2, n + 1):
    for j in range(1, i):
        dp[i] = min(prices[i], dp[i], dp[j] + dp[i - j])

print(dp[n])
