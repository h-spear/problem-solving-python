# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        for i in range(n):
            if nums[i] == 0:
                j = i
                for j in range(i + 1, n):
                    if nums[j]:
                        break
                nums[i], nums[j] = nums[j], nums[i]
