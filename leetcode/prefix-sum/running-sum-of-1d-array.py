# https://leetcode.com/problems/running-sum-of-1d-array/


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r_sum = [0] * n
        for i in range(n):
            r_sum[i] = r_sum[i - 1] + nums[i]
        return r_sum
