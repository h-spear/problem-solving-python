# https://www.acmicpc.net/problem/16139

import sys

input = lambda: sys.stdin.readline().rstrip()
s = input()
dp = [[0] * 26 for _ in range(len(s) + 1)]
questions = []

for idx, char in enumerate(s):
    for i in range(26):
        dp[idx][i] = dp[idx - 1][i]
    dp[idx][ord(char) - 97] += 1


q = int(input())
for _ in range(q):
    alpha, l, r = input().split()
    alpha = ord(alpha) - 97
    l = int(l)
    r = int(r)

    print(dp[r][alpha] - dp[l - 1][alpha])
