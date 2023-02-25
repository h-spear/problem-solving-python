# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0] = [-prices[0], 0]
        for i in range(1, n):
            price = prices[i]
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - price)
            dp[i][1] = max(dp[i - 1][0] + price - fee, dp[i - 1][1])

        return max(dp[n - 1])
