# https://www.acmicpc.net/problem/2294

INF = int(1e9)
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [INF] * 10001
dp[0] = 0

coins = list(set(coins))
coins.sort()
for coin in coins:
    if coin >= 10001:
        continue
    dp[coin] = 1

for i in range(coins[0], k + 1):
    MIN = INF
    if i in coins:
        continue
    for coin in coins:
        if i - coin >= coins[0]:
            MIN = min(dp[i - coin], MIN)
    dp[i] = MIN + 1

print(-1 if dp[k] == INF or dp[k] == INF + 1 else dp[k])
