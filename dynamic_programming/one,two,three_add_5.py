# https://www.acmicpc.net/problem/15990

p = 1000000009
dp = [[0] * 3 for _ in range(100010)]
dp[1][0] = 1
dp[2][1] = 1
dp[3][0], dp[3][1], dp[3][2] = 1, 1, 1
for i in range(4, 100010):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % p
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % p
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % p

for tc in range(int(input())):
    n = int(input())
    print(sum(dp[n]) % p)
