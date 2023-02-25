# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/403406/Python-easy-and-clear-solution.-Beginner-friendly.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        INF = float("inf")
        buy, sell, buycool, sellcool = -INF, 0, -INF, 0
        for price in prices:
            newbuy = sellcool - price
            newsell = max(buy, buycool) + price
            newbuycool = max(buy, buycool)
            newsellcool = max(sell, sellcool)
            buy, sell, buycool, sellcool = newbuy, newsell, newbuycool, newsellcool

        return max(sell, sellcool)
