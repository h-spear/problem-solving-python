# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/2555676/Python-Simple-DP-O(nk)-Uses-the-idea-of-%22reinvesting%22


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0

        profit = [0] * (k + 1)
        cost = [float("inf")] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                cost[i] = min(cost[i], price - profit[i - 1])
                profit[i] = max(profit[i], price - cost[i])

        return profit[k]
