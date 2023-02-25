# https://www.acmicpc.net/problem/15993

dp = [[0] * 2 for _ in range(100001)]
dp[1][0] = 1
dp[1][1] = 0
dp[2][0] = 1
dp[2][1] = 1
dp[3][0] = 2
dp[3][1] = 2
p = 1000000009

for i in range(4, 100001):
    dp[i][0] = (dp[i - 1][1] + dp[i - 2][1] + dp[i - 3][1]) % p
    dp[i][1] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 3][0]) % p

for tc in range(int(input())):
    n = int(input())
    print(*dp[n])
