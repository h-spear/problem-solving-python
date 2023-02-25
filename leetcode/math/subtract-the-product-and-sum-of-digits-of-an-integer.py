# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        summ = 0
        while n:
            num = n % 10
            product *= num
            summ += num
            n //= 10

        return product - summ
