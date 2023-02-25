# https://leetcode.com/problems/spiral-matrix-ii/


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        k = 1
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                matrix[top][j] = k
                k += 1
            top += 1

            for i in range(top, bottom + 1):
                matrix[i][right] = k
                k += 1
            right -= 1

            for j in range(right, left - 1, -1):
                matrix[bottom][j] = k
                k += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = k
                k += 1
            left += 1

        return matrix
