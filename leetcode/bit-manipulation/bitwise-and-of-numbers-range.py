# https://leetcode.com/problems/bitwise-and-of-numbers-range/


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if right >= left << 1:
            return 0

        res = left
        for i in range(left, right + 1):
            res &= i
        return res
