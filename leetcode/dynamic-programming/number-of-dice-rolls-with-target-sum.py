# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        p = 1000000007
        dp = [[0] * (max(target, k) + 1) for _ in range(n + 1)]

        for j in range(1, k + 1):
            dp[1][j] = 1

        for i in range(2, n + 1):
            for j in range(1, target + 1):
                for l in range(1, k + 1):
                    if j - l == 0:
                        break
                    dp[i][j] += dp[i - 1][j - l]
                    dp[i][j] %= p

        return dp[n][target]
