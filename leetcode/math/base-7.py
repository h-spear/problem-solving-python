# https://leetcode.com/problems/base-7/


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        absnum = abs(num)
        answer = ""
        while absnum:
            answer += str(absnum % 7)
            absnum //= 7

        if num < 0:
            answer += "-"

        return answer[::-1]
