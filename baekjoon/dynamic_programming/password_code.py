# https://www.acmicpc.net/problem/2011

import sys

sys.setrecursionlimit(5000)
p = 1_000_000
n = -1
cipher_text = None
dp = None


def dfs(idx):
    if idx >= n:
        return 1
    if dp[idx] != -1:
        return dp[idx]
    if cipher_text[idx] == 0:
        return 0

    dp[idx] = 0
    dp[idx] += dfs(idx + 1)
    if idx + 1 < n and 0 < cipher_text[idx] * 10 + cipher_text[idx + 1] < 27:
        dp[idx] += dfs(idx + 2)
    dp[idx] %= p
    return dp[idx]


def main():
    global n, cipher_text, dp
    cipher_text = list(map(int, input()))
    n = len(cipher_text)
    dp = [-1] * n
    print(dfs(0))


if __name__ == "__main__":
    main()
