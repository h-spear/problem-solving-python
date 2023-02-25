# https://leetcode.com/problems/sort-colors/
# sort in-place


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        for i in range(n):
            k = i
            minn = nums[i]
            for j in range(i + 1, n):
                if minn > nums[j]:
                    k = j
                    minn = nums[j]
            nums[i], nums[k] = nums[k], nums[i]

        return nums
