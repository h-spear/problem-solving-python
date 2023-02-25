# https://www.acmicpc.net/problem/14916


def solution(n):
    if n == 1 or n == 3:
        return -1
    if n == 2 or n == 5:
        return 1
    if n == 4:
        return 2

    INF = float("inf")
    dp = [INF] * (n + 1)
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    for i in range(6, n + 1):
        dp[i] = min(dp[i - 2] + 1, dp[i - 5] + 1, dp[i])

    return -1 if dp[n] == INF else dp[n]


n = int(input())
print(solution(n))
