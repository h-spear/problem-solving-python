# https://www.acmicpc.net/problem/11054


def lis_dp(A):
    n = len(A)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp


n = int(input())
A = list(map(int, input().split()))

dp1 = lis_dp(A)
dp2 = lis_dp(A[::-1])
answer = 0
for i in range(n):
    answer = max(answer, dp1[i] + dp2[n - i - 1] - 1)
print(answer)
