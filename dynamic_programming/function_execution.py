# https://www.acmicpc.net/problem/9184


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return table[20][20][20]
    return table[a][b][c]


def make_dp():
    dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
    for i in range(21):
        for j in range(21):
            for k in range(21):
                if i <= 0 or j <= 0 or k <= 0:
                    dp[i][j][k] = 1
                    continue

                if i < j and j < k:
                    dp[i][j][k] = (
                        dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]
                    )
                else:
                    dp[i][j][k] = (
                        dp[i - 1][j][k]
                        + dp[i - 1][j - 1][k]
                        + dp[i - 1][j][k - 1]
                        - dp[i - 1][j - 1][k - 1]
                    )
    return dp


table = make_dp()
while 1:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))
