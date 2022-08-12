# https://school.programmers.co.kr/learn/courses/30/lessons/42897
# 코딩테스트 고득점 Kit : Dynamic Programming


def solution(money):
    n = len(money)
    dp1 = [0] * n
    dp2 = [0] * n

    # select first
    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2, n):
        dp1[i] = max(dp1[i - 2] + money[i], dp1[i - 1])

    # not select first
    dp2[0] = -1
    dp2[1] = money[1]
    dp2[2] = max(dp2[1], money[2])
    for i in range(3, n):
        dp2[i] = max(dp2[i - 2] + money[i], dp2[i - 1])

    return max(dp1[n - 2], dp2[n - 1])
