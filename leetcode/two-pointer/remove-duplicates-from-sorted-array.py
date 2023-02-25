# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)

        while i < n and j < n:
            while j < n - 1:
                if nums[j] != nums[j + 1]:
                    break
                j += 1

            nums[i] = nums[j]
            i += 1
            j += 1

        return i
