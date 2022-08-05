# https://school.programmers.co.kr/learn/courses/30/lessons/12942


def solution(matrix_sizes):
    ms = matrix_sizes
    n = len(ms)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    INF = float("inf")
    for i in range(1, n):
        for j in range(n - i):
            x = j + i
            dp[j][j + i] = INF
            for k in range(j, x):
                dp[j][x] = min(
                    dp[j][x], dp[j][k] + dp[k + 1][x] + ms[j][0] * ms[k][1] * ms[x][1]
                )

    return dp[0][n - 1]
