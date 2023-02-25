# https://leetcode.com/problems/single-element-in-a-sorted-array/


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            l = max(0, mid - 1)
            r = min(n - 1, mid + 1)
            if mid != 0 and nums[l] == nums[mid]:
                if mid % 2 == 1:
                    left = mid + 1
                else:
                    right = mid - 2
            elif mid != n - 1 and nums[r] == nums[mid]:
                if (mid - 1) % 2 == 1:
                    left = mid + 2
                else:
                    right = mid - 1
            else:
                return nums[mid]

        return nums[left]
