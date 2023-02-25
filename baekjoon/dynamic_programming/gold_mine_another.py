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

    for c in range(1, m):
        for r in range(n):
            left = dp[r][c - 1]

            # 맨 위
            if r == 0:
                left_up = 0
            else:
                left_up = dp[r - 1][c - 1]

            if r == n - 1:
                left_down = 0
            else:
                left_down = dp[r + 1][c - 1]

            dp[r][c] = array[r][c] + max(left, left_down, left_up)

    result = 0
    for r in range(n):
        result = max(result, dp[r][m - 1])
    return result


for _ in range(t):
    n, m = map(int, input().split())
    input_data = list(map(int, input().split()))

    for i in range(len(input_data)):
        array[i // m][i % m] = input_data[i]

    print(max_gold(n, m))
