# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def f(x):
            res = 0
            for num in nums:
                res += math.ceil(num / x)

            return res

        left = 1
        right = 1234567
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            v = f(mid)
            if v > threshold:
                left = mid + 1
            else:
                answer = mid
                right = mid - 1

        return answer
