# https://leetcode.com/problems/maximum-sum-circular-subarray/
# https://www.techiedelight.com/ko/maximum-sum-circular-subarray/


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        def get_max_subarray_sum(nums):
            dp = [0] * n
            dp[0] = nums[0]
            for i in range(1, n):
                if dp[i - 1] + nums[i] > nums[i]:
                    dp[i] = dp[i - 1] + nums[i]
                else:
                    dp[i] = nums[i]
            return max(dp)

        reverse_sign_nums = nums.copy()
        for i in range(n):
            reverse_sign_nums[i] *= -1

        candidate1 = get_max_subarray_sum(nums)
        candidate2 = sum(nums) - (-1 * get_max_subarray_sum(reverse_sign_nums))

        return max(candidate1, candidate2) if candidate1 > 0 else candidate1
