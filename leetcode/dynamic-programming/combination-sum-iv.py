# https://leetcode.com/problems/combination-sum-iv/


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        _dp = [-1] * (target + 1)
        _dp[0] = 1

        def dp(x):
            if x == 0:
                return 1
            elif x < 0:
                return 0

            if _dp[x] != -1:
                return _dp[x]

            res = 0
            for num in nums:
                res += dp(x - num)
            _dp[x] = res
            return res

        return dp(target)
