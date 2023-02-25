# https://leetcode.com/problems/matrix-block-sum/


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        answer = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                answer[max(i - k, 0)][max(0, j - k)] += mat[i][j]
                answer[max(i - k, 0)][min(j + k + 1, n)] -= mat[i][j]
                answer[min(i + k + 1, m)][max(j - k, 0)] -= mat[i][j]
                answer[min(i + k + 1, m)][min(j + k + 1, n)] += mat[i][j]

        for i in range(m + 1):
            for j in range(1, n + 1):
                answer[i][j] += answer[i][j - 1]

        for j in range(n + 1):
            for i in range(1, m + 1):
                answer[i][j] += answer[i - 1][j]

        answer.pop()
        for i in range(m):
            answer[i].pop()

        return answer
