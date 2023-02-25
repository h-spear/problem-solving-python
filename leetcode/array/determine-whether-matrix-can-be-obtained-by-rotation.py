# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_degree_90(matrix):
            n = len(matrix)
            result = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    result[j][n - i - 1] = matrix[i][j]

            return result

        def check(matrix, target):
            n = len(matrix)
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] != target[i][j]:
                        return False
            return True

        if check(mat, target):
            return True

        for _ in range(3):
            mat = rotate_degree_90(mat)
            if check(mat, target):
                return True
        return False
