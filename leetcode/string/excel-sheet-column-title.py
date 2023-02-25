# https://leetcode.com/problems/excel-sheet-column-title/


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        _hash = {i: alpha for i, alpha in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        answer = ""
        while columnNumber:
            columnNumber -= 1
            answer += _hash[columnNumber % 26]
            columnNumber //= 26

        return answer[::-1]
