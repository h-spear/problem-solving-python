# https://leetcode.com/problems/next-greater-element-iii/

from itertools import permutations


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        MAX_INT = 2 ** 31
        numstr = str(n)
        answer = MAX_INT

        for candidate in permutations(numstr):
            num = int("".join(candidate))

            if num > MAX_INT:
                continue
            if num <= n:
                continue
            answer = min(answer, num)

        if answer == MAX_INT:
            return -1
        return answer
