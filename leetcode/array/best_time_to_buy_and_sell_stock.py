# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    # Kadane's Algorithm (O(n))
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = int(1e9)
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit

    # brute force
    # time limit exceeded O(n^2)
    def maxProfit_error(self, prices: list[int]) -> int:
        answer = 0
        for i, num in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if num < prices[j]:
                    answer = max(answer, prices[j] - num)
        return answer


answer = Solution()
print(answer.maxProfit([7, 1, 5, 3, 6, 4]))
