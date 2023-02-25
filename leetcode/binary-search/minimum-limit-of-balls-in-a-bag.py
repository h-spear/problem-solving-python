# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

import math


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def f(x):
            count = 0
            for num in nums:
                if num <= x:
                    continue
                count += math.ceil(num / x) - 1
            return count

        left = 1
        right = int(1e9)
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            count = f(mid)

            if count > maxOperations:
                left = mid + 1
            else:
                answer = mid
                right = mid - 1

        return answer
