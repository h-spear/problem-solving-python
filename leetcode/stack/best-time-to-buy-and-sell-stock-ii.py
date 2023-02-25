# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        answer = 0
        for price in prices:
            if not stack:
                stack.append(price)
                continue

            if stack[-1] < price:
                temp = stack.pop()
                stack.append(price)
                profit = price - temp
                answer += profit
            else:
                stack.append(price)

        return answer
