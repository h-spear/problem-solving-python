# https://programmers.co.kr/learn/courses/30/lessons/12913


def solution(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]
    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(n - 1):
        for j in range(4):
            for k in range(4):
                if j == k:
                    continue
                dp[i + 1][k] = max(dp[i][j] + land[i + 1][k], dp[i + 1][k])

    return max(dp[n - 1])
