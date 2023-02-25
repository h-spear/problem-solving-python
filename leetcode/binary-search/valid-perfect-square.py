# https://leetcode.com/problems/valid-perfect-square/


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            mid = (left + right) // 2
            temp = num / mid

            if temp > mid:
                left = mid + 1
            elif temp < mid:
                right = mid - 1
            else:
                return True

        return False
