# https://www.acmicpc.net/problem/18353
# 최장 증가 부분 수열(LIS, Longest Increasing Subsequence)

n = int(input())
data = list(map(int, input().split()))
data.reverse()
print(data)

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
