# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0)
        dp = [[0] * (n + 1) for _ in range(2)]
        for i in range(n):
            if nums[i] == 0:
                dp[0][i], dp[1][i] = 0, 0
            elif nums[i] > 0:
                if nums[i - 1] == 0:
                    dp[0][i], dp[1][i] = 0, 1
                elif dp[0][i - 1] == 0:
                    dp[0][i], dp[1][i] = 0, dp[1][i - 1] + 1
                else:
                    dp[0][i], dp[1][i] = dp[0][i - 1] + 1, dp[1][i - 1] + 1
            else:
                if nums[i - 1] == 0:
                    dp[0][i], dp[1][i] = 1, 0
                elif dp[0][i - 1] == 0:
                    dp[0][i], dp[1][i] = dp[1][i - 1] + 1, 0
                else:
                    dp[0][i], dp[1][i] = dp[1][i - 1] + 1, dp[0][i - 1] + 1

        return max(dp[1])
