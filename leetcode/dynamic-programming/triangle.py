# https://leetcode.com/problems/triangle/
# Runtime: 58 ms, faster than 99.78% of Python3 online submissions for Triangle.


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]

        for i in range(1, n):
            temp = [0] * n
            for j in range(i + 1):
                if j == 0:
                    temp[0] = dp[0] + triangle[i][0]
                elif j == i:
                    temp[i] = dp[i - 1] + triangle[i][i]
                else:
                    temp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]

            dp = temp

        return min(dp)
