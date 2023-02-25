# https://www.acmicpc.net/problem/5557

n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * (n - 1) for _ in range(21)]
dp[nums[0]][0] = 1
for i in range(len(nums) - 1):
    now = nums[i]
    for j in range(21):
        cnt = dp[j][i - 1]
        if cnt == 0:
            continue

        if j - now >= 0:
            dp[j - now][i] += cnt
        if j + now <= 20:
            dp[j + now][i] += cnt

print(dp[nums[-1]][n - 2])
