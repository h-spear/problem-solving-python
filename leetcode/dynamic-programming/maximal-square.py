# https://leetcode.com/problems/maximal-square/


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if matrix[i][0] == "1":
                dp[i][0] = 1

        for j in range(n):
            if matrix[0][j] == "1":
                dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "0":
                    continue

                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        maxx = 0
        for x in dp:
            maxx = max(maxx, max(x))

        return maxx ** 2
