# https://programmers.co.kr/learn/courses/30/lessons/12907


def solution(n, money):
    money.sort()
    p = 1000000007
    lm = len(money)
    dp = [[0] * lm for _ in range(n + 1)]
    for i in range(lm):
        dp[money[i]][i] = 1

    for i in range(1, n):
        curr = 0

        for j in range(lm):
            if i + money[j] > n:
                break
            curr = (curr + dp[i][j]) % p
            dp[i + money[j]][j] += curr
            dp[i + money[j]][j] %= p

    return sum(dp[n]) % p
