# https://leetcode.com/problems/excel-sheet-column-number/


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        _hash = {alpha: i + 1 for i, alpha in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        while columnTitle:
            answer *= 26
            answer += _hash[columnTitle[0]]
            columnTitle = columnTitle[1:]

        return answer
