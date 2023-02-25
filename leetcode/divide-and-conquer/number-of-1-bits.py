# https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        def divide_and_conquer(l, r):
            if l == r:
                return 1 if n & 1 << r else 0

            mid = (l + r) // 2
            return divide_and_conquer(l, mid) + divide_and_conquer(mid + 1, r)

        return divide_and_conquer(0, 31)
