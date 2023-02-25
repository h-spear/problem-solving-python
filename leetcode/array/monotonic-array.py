# https://leetcode.com/problems/monotonic-array/


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        n = len(nums)

        inc = True
        dec = True
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                inc = False

            if nums[i] < nums[i + 1]:
                dec = False

        return inc or dec
