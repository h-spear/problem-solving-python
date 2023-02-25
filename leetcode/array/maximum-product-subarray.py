# https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        answer = nums[0]
        dp = [[0] * 2 for _ in range(n)]
        dp[0] = [nums[0], nums[0]]

        for i in range(1, n):
            dp[i][0] = nums[i] * min(1, dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = nums[i] * max(1, dp[i - 1][0], dp[i - 1][1])

        for r in dp:
            answer = max(answer, max(r))
        return answer
