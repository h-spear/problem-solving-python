# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
                answer = mid
            else:
                left = mid + 1
        return answer
