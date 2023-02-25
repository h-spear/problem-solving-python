# https://leetcode.com/problems/pascals-triangle-ii/


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        dp = [1, 1]

        for i in range(2, rowIndex + 1):
            temp = [1]
            for j in range(i - 1):
                temp.append(dp[j] + dp[j + 1])

            temp.append(1)
            dp = temp

        return dp
