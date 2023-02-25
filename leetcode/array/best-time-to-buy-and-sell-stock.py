# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = 1234567
        answer = 0
        for price in prices:
            if price <= minn:
                minn = price
            else:
                answer = max(answer, price - minn)

        return answer
