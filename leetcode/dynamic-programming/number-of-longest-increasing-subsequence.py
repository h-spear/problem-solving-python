# https://leetcode.com/problems/number-of-longest-increasing-subsequence/


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        counter = [1] * n

        for i, num in enumerate(nums):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue

                if dp[i] < dp[j] + 1:
                    counter[i] = counter[j]
                    dp[i] = dp[j] + 1
                elif dp[i] == dp[j] + 1:
                    counter[i] += counter[j]

        maxx = max(dp)
        answer = 0
        print(dp)
        print(counter)
        for i in range(n):
            if dp[i] == maxx:
                answer += counter[i]

        return answer
