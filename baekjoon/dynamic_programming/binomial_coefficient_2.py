# https://www.acmicpc.net/problem/11051
# (n+1)C(k+1) = nCk + nC(k+1)


def solution(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
        dp[i][1] = i

    for _k in range(2, k + 1):
        for _n in range(_k, n + 1):
            dp[_n][_k] = (dp[_n - 1][_k - 1] + dp[_n - 1][_k]) % 10007

    return dp[n][k]


n, k = map(int, input().split())
print(solution(n, k))
