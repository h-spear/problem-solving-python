# https://leetcode.com/problems/search-a-2d-matrix/


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] > target or matrix[i][n - 1] < target:
                continue

            for j in range(n):
                if matrix[i][j] == target:
                    return True

        return False
