# https://leetcode.com/problems/valid-triangle-number/

from bisect import bisect_left


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        answer = 0
        for i in range(n):
            for j in range(i + 1, n - 1):

                key = nums[i] + nums[j]
                answer += bisect_left(nums, key, lo=j + 1) - j - 1

                # TLE
                # answer += bisect_left(nums[j + 1 :], key)

        return answer
