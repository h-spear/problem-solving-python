# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        lenS = len(s)
        table = [[""] * (1001) for _ in range(numRows + 1)]

        i = 0
        j = 0
        flag = True
        for char in s:
            table[i][j] = char

            if flag:
                i += 1
                if i == numRows - 1:
                    flag = False
            else:
                i -= 1
                j += 1
                if i == 0:
                    flag = True

        answer = ""

        for row in table:
            answer += "".join(row)

        return answer
