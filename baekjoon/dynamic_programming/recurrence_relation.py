# https://www.acmicpc.net/problem/13699

dp = [0] * 36
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 36):
    temp = 0
    for j in range(i // 2):
        temp += (dp[j] * dp[i - j - 1]) * 2

    if i & 1 == 1:
        temp += dp[i // 2] ** 2

    dp[i] = temp

print(dp[int(input())])
