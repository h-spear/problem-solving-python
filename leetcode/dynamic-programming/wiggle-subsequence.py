# https://leetcode.com/problems/wiggle-subsequence/


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] == nums[j]:
                    pass
                elif nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                else:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)

        answer = 0
        for x in dp:
            answer = max(answer, max(x))

        return answer + 1
