# https://www.acmicpc.net/problem/9084


def solve(n, coin, amount):
    dp = [[0] * 21 for _ in range(10001)]

    for i, c in enumerate(coin):
        dp[c][i] = 1

    for i in range(amount + 1):
        for j in range(n):
            if i - coin[j] < 0:
                continue
            dp[i][j] = max(sum(dp[i - coin[j]][: j + 1]), dp[i][j])

    return sum(dp[amount])


for tc in range(int(input())):
    n = int(input())
    coin = list(map(int, input().split()))
    amount = int(input())
    print(solve(n, coin, amount))
