# https://leetcode.com/problems/ugly-number-iii/


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def f(x):
            return (
                (x // a + x // b + x // c)
                - (x // lcm_ab + x // lcm_bc + x // lcm_ac)
                + (x // lcm_abc)
            )

        a, b, c = sorted([a, b, c])
        lcm_ab = self._lcm(a, b)
        lcm_bc = self._lcm(b, c)
        lcm_ac = self._lcm(a, c)
        lcm_abc = self._lcm(lcm_ab, c)

        left = 1
        right = 2 * int(1e9)
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if f(mid) < n:
                left = mid + 1
            else:
                answer = mid
                right = mid - 1

        return answer

    def _gcd(self, x, y):
        if x % y == 0:
            return y
        else:
            return self._gcd(y, x % y)

    def _lcm(self, x, y):
        return (x * y) // self._gcd(x, y)
