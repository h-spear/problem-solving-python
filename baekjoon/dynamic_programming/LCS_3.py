# https://www.acmicpc.net/problem/1958

str1 = input()
str2 = input()
str3 = input()
l1 = len(str1)
l2 = len(str2)
l3 = len(str3)

dp = [[[0] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        for k in range(1, l3 + 1):
            if str1[i - 1] == str2[j - 1] == str3[k - 1]:
                dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1]
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

answer = 0
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        answer = max(max(dp[i][j]), answer)

print(answer)
