# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        p = 1000000007
        s = ""
        i = 1
        while i <= n:
            s += bin(i)[2:]
            i += 1

        return int(s, 2) % p
