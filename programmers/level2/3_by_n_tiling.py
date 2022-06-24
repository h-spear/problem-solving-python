# https://programmers.co.kr/learn/courses/30/lessons/12902?language=python3


def solution(n):
    p = 1000000007
    dp = [0] * (2 * n + 1)
    dp[0] = 1
    dp[2] = 3
    dp[4] = 11
    sub = dp[2] + dp[0]
    for i in range(6, 2 * n + 1, 2):
        dp[i] = (3 * dp[i - 2] + 2 * sub) % p
        sub += dp[i - 2]

    return dp[n]
