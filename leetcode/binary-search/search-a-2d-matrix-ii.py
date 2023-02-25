# https://leetcode.com/problems/search-a-2d-matrix-ii/

from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            first = matrix[i][0]
            last = matrix[i][-1]

            if target < first or target > last:
                continue

            idx = bisect_left(matrix[i], target)
            if idx < n and matrix[i][idx] == target:
                return True

        return False
