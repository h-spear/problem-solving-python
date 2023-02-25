# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        numstr = str(x)
        if numstr == numstr[::-1]:
            return True
        return False
