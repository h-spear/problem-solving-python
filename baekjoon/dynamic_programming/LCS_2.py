# https://www.acmicpc.net/problem/9252

import sys

input = lambda: sys.stdin.readline().rstrip()
word1 = input()
word2 = input()

m = len(word1)
n = len(word2)
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[m][n])

if dp[m][n]:
    i = m
    j = n
    answer = ""
    while i > 0 and j > 0:
        if word1[i - 1] == word2[j - 1]:
            answer += word1[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    print(answer[::-1])
