# https://leetcode.com/problems/range-sum-query-2d-immutable/


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        dp = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                dp[i][j] = dp[i][j - 1] + matrix[i][j]

        for j in range(self.n):
            for i in range(1, self.m):
                dp[i][j] += dp[i - 1][j]

        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp[row2][col2]
            - self.dp[row2][col1 - 1]
            - self.dp[row1 - 1][col2]
            + self.dp[row1 - 1][col1 - 1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
