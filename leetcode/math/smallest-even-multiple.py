# https://leetcode.com/problems/smallest-even-multiple/


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def _gcd(a, b):
            if a % b == 0:
                return b
            else:
                return _gcd(b, a % b)

        return 2 * n // _gcd(2, n)
