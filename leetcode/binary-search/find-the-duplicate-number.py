# https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x):
            count = 0
            for num in nums:
                if num <= x:
                    count += 1
            return count

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if f(mid) > mid:
                right = mid - 1
            else:
                left = mid + 1

        return left
