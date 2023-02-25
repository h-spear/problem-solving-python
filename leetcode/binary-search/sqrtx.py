# https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            square = mid ** 2
            if square > x:
                right = mid - 1
            else:
                answer = mid
                left = mid + 1

        return answer
