# https://leetcode.com/problems/longest-palindromic-subsequence/
# https://leetcode.com/problems/longest-palindromic-subsequence/discuss/2461810/Simple-DP-solution-with-Python-3
# 98.20%


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def helper(left, right):

            if left > right:
                return 0

            if dp[left][right] != -1:
                return dp[left][right]

            if left == right:
                return 1

            res = 0
            if s[left] == s[right]:
                res = 2 + helper(left + 1, right - 1)
            else:
                res = max(helper(left + 1, right), helper(left, right - 1))

            dp[left][right] = res
            return res

        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        return helper(0, n - 1)
