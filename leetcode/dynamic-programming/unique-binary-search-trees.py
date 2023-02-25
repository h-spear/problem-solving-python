# https://leetcode.com/problems/unique-binary-search-trees/


class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * 20
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] += 2 * dp[i - 1]
            for j in range(1, n):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]
