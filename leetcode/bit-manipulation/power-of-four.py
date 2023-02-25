# https://leetcode.com/problems/power-of-four/


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False

        count = 0
        i = -1
        while n:
            if n & 1:
                count += 1

            i += 1
            n >>= 1

            if count >= 2:
                return False

        return i & 1 == 0
