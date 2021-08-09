# https://www.acmicpc.net/problem/7620
# ????


def min_distance(ed, n, m):
    paths = [(n, m)]
    while n != 0 and m != 0:
        minimum = min(ed[n - 1][m], ed[n][m - 1], ed[n - 1][m - 1])
        if minimum == ed[n - 1][m]:
            n -= 1
        elif minimum == ed[n][m - 1]:
            m -= 1
        else:
            n -= 1
            m -= 1
        paths.append((n, m))
    return paths


def edit_distance(str1, str2):
    short = str2 if len(str1) - len(str2) > 0 else str1
    long = str1 if len(str1) - len(str2) > 0 else str2
    m = len(long)
    n = len(short)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for r in range(1, n + 1):
        dp[r][0] = r
    for c in range(1, m + 1):
        dp[0][c] = c

    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if short[r - 1] == long[c - 1]:
                dp[r][c] = dp[r - 1][c - 1]
            else:
                dp[r][c] = 1 + min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1])

    paths = min_distance(dp, n, m)
    x, y = paths.pop()

    while paths:
        next_x, next_y = paths.pop()
        if next_x - x == 1 and next_y - y == 1:
            if dp[next_x][next_y] - dp[x][y] == 0:
                print("c ", short[x])
            else:
                print("m ", long[y])
        elif next_x - x == 0:
            print("a ", long[y])
        elif next_y - y == 0:
            print("d ", long[y])

        x, y = next_x, next_y
    return


edit_distance(input(), input())
