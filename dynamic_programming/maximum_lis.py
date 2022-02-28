# https://www.acmicpc.net/problem/11055

n = int(input())
A = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    dp[i] = A[i]
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))
