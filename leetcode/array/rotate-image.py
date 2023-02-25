# https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for k in range(1, int(n / 2) + 1):
            l = n - 2 * k + 1
            for _ in range(l):
                temp = matrix[k - 1][k - 1]
                for i in range(k, n - k + 1):
                    matrix[i - 1][k - 1] = matrix[i][k - 1]

                for j in range(k, n - k + 1):
                    matrix[n - k][j - 1] = matrix[n - k][j]

                for i in range(n - k, k - 1, -1):
                    matrix[i][n - k] = matrix[i - 1][n - k]

                for j in range(n - k, k - 1, -1):
                    matrix[k - 1][j] = matrix[k - 1][j - 1]

                matrix[k - 1][k] = temp
