t = int(input())

array = [[0] * 20 for _ in range(20)]
dp = [[0] * 20 for _ in range(20)]


def cleanDP(n, m):
    for i in range(n):
        for j in range(m):
            dp[i][j] = 0


def max_gold(n, m):
    cleanDP(n, m)

    for r in range(n):
        dp[r][0] = array[r][0]

    for c in range(m - 1):
        for r in range(n):
            now = dp[r][c]
            if r + 1 < n:
                dp[r + 1][c + 1] = max(dp[r + 1][c + 1], now + array[r + 1][c + 1])
            if r - 1 >= 0:
                dp[r - 1][c + 1] = max(dp[r - 1][c + 1], now + array[r - 1][c + 1])
            dp[r][c + 1] = max(dp[r][c + 1], now + array[r][c + 1])

    result = -1
    for r in range(n):
        result = max(result, dp[r][m - 1])
    return result


for _ in range(t):
    n, m = map(int, input().split())
    input_data = list(map(int, input().split()))

    for i in range(len(input_data)):
        array[i // m][i % m] = input_data[i]

    print(max_gold(n, m))
