# https://www.acmicpc.net/problem/11060

n = int(input())
INF = 1000000
jump = list(map(int, input().split()))
dp = [INF] * n
dp[0] = 0
for i in range(n):
    for j in range(1, jump[i] + 1):
        if i + j >= n:
            continue
        dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[n - 1] == INF:
    print(-1)
else:
    print(dp[n - 1])
