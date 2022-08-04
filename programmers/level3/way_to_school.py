# https://programmers.co.kr/learn/courses/30/lessons/42898
# 코딩테스트 고득점 Kit : Dynamic Programming


def solution(m, n, puddles):
    p = 1000000007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        if [1, i] in puddles:
            break
        dp[i][1] = 1
    for j in range(1, m + 1):
        if [j, 1] in puddles:
            break
        dp[1][j] = 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if [j, i] in puddles:
                continue
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % p

    return dp[n][m]
