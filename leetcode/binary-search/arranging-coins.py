# https://leetcode.com/problems/arranging-coins/


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        answer = 0
        while left <= right:
            mid = (left + right) // 2

            temp = (mid * (mid + 1)) // 2
            if temp > n:
                right = mid - 1
            else:
                answer = mid
                left = mid + 1

        return answer
