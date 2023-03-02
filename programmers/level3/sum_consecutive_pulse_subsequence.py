# https://school.programmers.co.kr/learn/courses/30/lessons/161988


def get_max(n, sequence, purse):
    dp = [0] * n
    dp[0] = sequence[0] * purse[0]

    maxx = dp[0]
    for i in range(1, n):
        value = sequence[i] * purse[i]
        if dp[i - 1] + value > value:
            dp[i] = dp[i - 1] + value
        else:
            dp[i] = value
        maxx = max(maxx, dp[i])

    return maxx


def solution(sequence):
    n = len(sequence)
    purse = [-1, 1] * (n // 2 + 10)
    return max(get_max(n, sequence, purse), get_max(n, sequence, purse[1:]))
