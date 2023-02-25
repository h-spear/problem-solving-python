# https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i + coin > amount:
                    continue

                dp[i + coin] = min(dp[i + coin], dp[i] + 1)

        if dp[amount] == float("inf"):
            return -1
        return dp[amount]
