# https://leetcode.com/problems/pascals-triangle/


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        pascal = [[1], [1, 1]]

        for i in range(3, numRows + 1):
            temp = [1]
            for j in range(i - 2):
                temp.append(pascal[i - 2][j] + pascal[i - 2][j + 1])
            temp.append(1)
            pascal.append(temp)

        return pascal
