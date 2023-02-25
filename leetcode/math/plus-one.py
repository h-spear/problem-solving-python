# https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def add(i):
            if i < 0:
                digits.appendleft(1)
                return

            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                add(i - 1)

        digits = deque(digits)
        n = len(digits)
        add(n - 1)

        return list(digits)
