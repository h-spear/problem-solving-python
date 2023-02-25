# https://leetcode.com/problems/find-pivot-index/


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        psum = [0] * (n + 2)
        for i in range(1, n + 1):
            psum[i] = psum[i - 1] + nums[i - 1]

        for i in range(1, n + 1):
            if psum[i - 1] == psum[n] - psum[i]:
                return i - 1
        return -1
