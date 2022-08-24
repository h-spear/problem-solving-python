# https://school.programmers.co.kr/learn/courses/30/lessons/12983


def solution(strs, t):
    INF = float("inf")
    lt = len(t)
    str_set = set(strs)
    dp = [INF] * (lt + 10)

    for _str in strs:
        ls = len(_str)
        if t[:ls] == _str:
            dp[ls - 1] = 1

    for i in range(1, lt):
        for j in range(0, 5):
            if i - j < 0:
                continue
            find = t[i - j : i + 1]
            if find in str_set:
                dp[i] = min(dp[i - j - 1] + 1, dp[i])

    if dp[lt - 1] == INF:
        return -1
    return dp[lt - 1]
