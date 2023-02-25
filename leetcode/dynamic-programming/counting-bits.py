# https://leetcode.com/problems/counting-bits/


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0] * (n + 1)
        dp[1] = 1
        j = 1
        for i in range(2, n + 1):
            c = i % j
            if c == 0:
                j <<= 1
                dp[i] = 1
            else:
                dp[i] = dp[c] + dp[i - c]
        return dp
