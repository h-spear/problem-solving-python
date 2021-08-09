# 편집 거리 알고리즘
# Levenshtein Distance, Edit Distance


def edit_distance(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for r in range(1, n + 1):
        dp[r][0] = r
    for c in range(1, m + 1):
        dp[0][c] = c

    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if str1[r - 1] == str2[c - 1]:
                dp[r][c] = dp[r - 1][c - 1]
            else:
                dp[r][c] = 1 + min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1])

    return dp[r][c]


print(edit_distance(input(), input()))
