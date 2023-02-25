# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def func(x):
            cnt = 0
            for num in nums:
                if num >= x:
                    cnt += 1
            return cnt

        left = 0
        right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            cnt = func(mid)

            if cnt == mid:
                return mid
            elif cnt > mid:
                left = mid + 1
            else:
                right = mid - 1

        return -1
