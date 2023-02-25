# https://leetcode.com/problems/maximum-length-of-repeated-subarray/


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
        answer = 0
        for i in range(n + 1):
            answer = max(answer, max(dp[i]))

        return answer
