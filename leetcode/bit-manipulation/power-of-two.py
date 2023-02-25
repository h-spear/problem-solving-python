# https://leetcode.com/problems/power-of-two/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1

            if count >= 2:
                return False
        return count == 1
