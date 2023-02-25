# https://leetcode.com/problems/integer-break/


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * 60
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            for j in range(1, (i // 2) + 1):
                one = max(i - j, dp[i - j])
                two = max(j, dp[j])
                dp[i] = max(dp[i], one * two)

        return dp[n]
