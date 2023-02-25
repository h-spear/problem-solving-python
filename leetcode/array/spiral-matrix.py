# https://leetcode.com/problems/spiral-matrix/


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n - 1
        top, bottom = 0, m - 1
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                order.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                order.append(matrix[i][right])
            right -= 1

            for j in range(right, left - 1, -1):
                order.append(matrix[bottom][j])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                order.append(matrix[i][left])
            left += 1

        return order[: n * m]
