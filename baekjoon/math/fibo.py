# https://www.acmicpc.net/problem/2747

dp = [0] * 46
dp[1] = 1


def fibo(n):
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print(fibo(int(input())))
