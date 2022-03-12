# https://www.acmicpc.net/problem/11568

n = int(input())
elem = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if elem[j] >= elem[i]:
            continue
        dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
