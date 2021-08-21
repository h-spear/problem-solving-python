# https://www.acmicpc.net/problem/11053
# https://www.acmicpc.net/problem/14002
# https://www.acmicpc.net/problem/14003
# 최장 증가 부분 수열, Longest Increasing Subsequence
# O(n^2)

n = int(input())
array = list(map(int, input().split()))

dp = [1] * (n)
for i in range(len(array)):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[j] + 1, dp[i])

now = max(dp)
print(now)
answer = []
for i in range(n - 1, -1, -1):
    if dp[i] == now:
        answer.append(array[i])
        now -= 1

for x in sorted(answer):
    print(x, end=" ")
