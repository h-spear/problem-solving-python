# https://leetcode.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        answer = n

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid - 1
                answer = mid
            else:
                left = mid + 1

        return answer
