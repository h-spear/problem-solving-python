# https://leetcode.com/problems/sort-the-matrix-diagonally/
# Runtime: 78 ms, faster than 99.19% of Python3 online submissions for Sort the Matrix Diagonally.


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            temp = []
            for j in range(min(n, m - i)):
                temp.append(mat[i + j][j])
            temp.sort()
            idx = 0
            for j in range(min(n, m - i)):
                result[i + j][j] = temp[idx]
                idx += 1

        for j in range(1, n):
            temp = []
            for i in range(min(m, n - j)):
                temp.append(mat[i][i + j])
            temp.sort()
            idx = 0
            for i in range(min(m, n - j)):
                result[i][i + j] = temp[idx]
                idx += 1

        return result
