# https://www.acmicpc.net/problem/15989

dp = [[0, 0, 0] for _ in range(10001)]
dp[1] = [1, 0, 0]
dp[2] = [1, 1, 0]
dp[3] = [2, 0, 1]

for i in range(4, 10001):
    dp[i] = [
        sum(dp[i - 1]),
        dp[i - 2][1] + dp[i - 2][2],
        dp[i - 3][2],
    ]

for tc in range(int(input())):
    print(sum(dp[int(input())]))
