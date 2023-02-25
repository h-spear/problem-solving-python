# https://leetcode.com/problems/add-digits/


class Solution:
    def addDigits(self, num: int) -> int:
        return num % 9 if (num % 9 != 0 or num == 0) else 9


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(map(int, list(str(num))))
        return num
