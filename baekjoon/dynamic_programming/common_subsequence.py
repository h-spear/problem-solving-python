# https://www.acmicpc.net/problem/5582
# LCS(Longest Common Subsequence) 문제와 약간 다르다.
# LCS : https://www.acmicpc.net/problem/9251


str1 = input()
str2 = input()
l1 = len(str1)
l2 = len(str2)
dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
answer = 0
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if str1[i - 1] != str2[j - 1]:
            continue

        dp[i][j] = 1 + dp[i - 1][j - 1]
        answer = max(answer, dp[i][j])

print(answer)
