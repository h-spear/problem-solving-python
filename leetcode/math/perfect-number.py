# https://leetcode.com/problems/perfect-number/


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        def get_divisors_sum(num):
            divisors = [1]
            for i in range(2, int(num ** 0.5) + 1):
                if num % i:
                    continue
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
            return sum(divisors)

        return num == get_divisors_sum(num)
