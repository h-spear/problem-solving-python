# https://leetcode.com/problems/reshape-the-matrix/


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat

        temp = []
        reshaped = [[0] * c for _ in range(r)]
        cnt = 0

        for i in range(m):
            for j in range(n):
                temp.append(mat[i][j])

        for i in range(r):
            for j in range(c):
                reshaped[i][j] = temp[cnt]
                cnt += 1

        return reshaped
