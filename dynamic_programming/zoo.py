# https://www.acmicpc.net/problem/1309

p = 9901


def solution(n):
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1][0], dp[1][1], dp[1][2] = 1, 1, 1

    for i in range(2, n + 1):
        dp[i][0] = sum(dp[i - 1]) % p
        dp[i][1] = dp[i - 1][0] + dp[i - 1][2] % p
        dp[i][2] = dp[i - 1][0] + dp[i - 1][1] % p

    return sum(dp[n]) % p


n = int(input())
print(solution(n))
