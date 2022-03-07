# https://www.acmicpc.net/problem/15624

p = 1000000007


def solution(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % p
    return dp[n]


n = int(input())
print(solution(n))
