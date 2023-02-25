# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -(2 ** 31)

        sign = -1 if x < 0 else 1

        reverse_x_str = str(abs(x))[::-1]
        reverse_x = int(reverse_x_str)

        if reverse_x < INT_MIN or reverse_x > INT_MAX:
            return 0
        return sign * reverse_x
