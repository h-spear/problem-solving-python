# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = high - low + 1
        if n & 1:
            if low & 1:
                return n // 2 + 1
            return n // 2
        else:
            return n // 2
