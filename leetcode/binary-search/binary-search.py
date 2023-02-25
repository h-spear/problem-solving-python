# https://leetcode.com/problems/binary-search/

from bisect import bisect_left


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        idx = bisect_left(nums, target)

        if idx < n and nums[idx] == target:
            return idx
        return -1
