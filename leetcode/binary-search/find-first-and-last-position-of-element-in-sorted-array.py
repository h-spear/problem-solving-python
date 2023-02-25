# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        upper_bound = 0
        lower_bound = 0

        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid - 1
                lower_bound = mid
            else:
                left = mid + 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
                upper_bound = mid
            else:
                right = mid - 1

        if nums[upper_bound] != target or nums[lower_bound] != target:
            return [-1, -1]
        return [lower_bound, upper_bound]


# library
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        upper_bound = bisect_right(nums, target) - 1
        lower_bound = bisect_left(nums, target)

        if nums[upper_bound] != target or nums[lower_bound] != target:
            return [-1, -1]
        return [lower_bound, upper_bound]
