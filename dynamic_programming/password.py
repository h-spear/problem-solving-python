# https://www.acmicpc.net/problem/2780

n = 1000
dp = [[0] * 10 for _ in range(n + 1)]
p = 1234567
for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][7]) % p
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][4]) % p
    dp[i][2] = (dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][5]) % p
    dp[i][3] = (dp[i - 1][2] + dp[i - 1][6]) % p
    dp[i][4] = (dp[i - 1][1] + dp[i - 1][5] + dp[i - 1][7]) % p
    dp[i][5] = (dp[i - 1][2] + dp[i - 1][4] + dp[i - 1][6] + dp[i - 1][8]) % p
    dp[i][6] = (dp[i - 1][3] + dp[i - 1][5] + dp[i - 1][9]) % p
    dp[i][7] = (dp[i - 1][4] + dp[i - 1][8] + dp[i - 1][0]) % p
    dp[i][8] = (dp[i - 1][5] + dp[i - 1][7] + dp[i - 1][9]) % p
    dp[i][9] = (dp[i - 1][6] + dp[i - 1][8]) % p

for tc in range(int(input())):
    n = int(input())
    print(sum(dp[n]) % p)
