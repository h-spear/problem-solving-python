# https://www.acmicpc.net/problem/2293

n, k = map(int, input().split())
coins = []
dp = [0] * (k + 1)
dp[0] = 1

for _ in range(n):
    coins.append(int(input()))
coins.sort()

for coin in coins:
    for i in range(coin, k + 1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]

print(dp[k])
