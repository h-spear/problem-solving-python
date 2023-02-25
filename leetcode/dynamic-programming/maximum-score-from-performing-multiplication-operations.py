# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

# tabulation
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                one = nums[left] * multipliers[i] + dp[i + 1][left + 1]
                two = nums[n - 1 - (i - left)] * multipliers[i] + dp[i + 1][left]
                dp[i][left] = max(one, two)

        return dp[0][0]


# TLE
# recursion + memorization

from collections import defaultdict


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        _dp = defaultdict(int)

        def dp(left, right, idx):
            if idx == len(multipliers):
                _dp[(left, right)] = 0
                return 0
            if (left, right) in _dp:
                return _dp[(left, right)]

            one = nums[left] * multipliers[idx] + dp(left + 1, right, idx + 1)
            two = nums[right] * multipliers[idx] + dp(left, right - 1, idx + 1)
            _dp[(left, right)] = max(one, two)
            return max(one, two)

        return dp(0, len(nums) - 1, 0)
