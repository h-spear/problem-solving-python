# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursionPow(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x

            temp = recursionPow(x, n // 2)
            if n & 1:
                return temp * temp * x
            else:
                return temp * temp

        if n < 0:
            return 1 / recursionPow(x, -n)
        return recursionPow(x, n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n
