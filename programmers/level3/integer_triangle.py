# https://programmers.co.kr/learn/courses/30/lessons/43105
# 코딩테스트 고득점 Kit : Dynamic Programming


def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(n - 1):
        for j in range(i + 1):
            dp[i + 1][j] = max(dp[i + 1][j], triangle[i + 1][j] + dp[i][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], triangle[i + 1][j + 1] + dp[i][j])

    return max(dp[n - 1])
