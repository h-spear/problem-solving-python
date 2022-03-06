# https://www.acmicpc.net/problem/9507

dp = [0] * 68
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 68):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

for tc in range(int(input())):
    n = int(input())
    print(dp[n])
