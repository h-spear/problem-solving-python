# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def f(length):
            for i in range(length - 1, m):
                for j in range(length - 1, n):
                    summation = (
                        psum[i][j]
                        - psum[i - length][j]
                        - psum[i][j - length]
                        + psum[i - length][j - length]
                    )
                    if summation <= threshold:
                        return True
            return False

        m = len(mat)
        n = len(mat[0])
        psum = [[0] * (n + 1) for _ in range(m + 1)]
        answer = 0

        for i in range(m):
            for j in range(n):
                psum[i][j] = psum[i][j - 1] + mat[i][j]

        for j in range(n):
            for i in range(1, m):
                psum[i][j] += psum[i - 1][j]

        left = 0
        right = min(m, n)
        while left <= right:
            mid = (left + right) // 2

            if f(mid):
                left = mid + 1
                answer = mid
            else:
                right = mid - 1

        return answer
