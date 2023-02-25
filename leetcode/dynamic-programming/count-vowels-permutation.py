# https://leetcode.com/problems/count-vowels-permutation/


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        p = int(1e9) + 7
        dp = [[0] * 5 for _ in range(n + 1)]
        dp[1] = [1, 1, 1, 1, 1]
        for i in range(2, n + 1):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % p
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % p
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % p
            dp[i][3] = (dp[i - 1][2]) % p
            dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % p

        return sum(dp[n]) % p
