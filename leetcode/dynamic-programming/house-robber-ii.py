# https://leetcode.com/problems/house-robber-ii/


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        dp1 = [0] * (n + 10)
        dp2 = [0] * (n + 10)

        # select first house
        dp1[0] = nums[0]
        dp1[1] = dp1[0]
        for i in range(2, n):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])

        # no select first house
        dp2[0] = 0
        dp2[1] = nums[1]
        dp2[2] = max(dp2[1], nums[2])
        for i in range(3, n):
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])

        return max(dp1[n - 2], dp2[n - 1])
