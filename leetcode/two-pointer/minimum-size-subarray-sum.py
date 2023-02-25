# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = float("inf")
        answer = INF
        n = len(nums)
        i = 0
        j = 1
        curr = nums[0]
        while i < j and j < n:
            if curr >= target:
                answer = min(answer, j - i)
                curr -= nums[i]
                i += 1
            else:
                curr += nums[j]
                j += 1

        while i != j:
            if curr >= target:
                answer = min(answer, j - i)

            curr -= nums[i]
            i += 1

        if answer == INF:
            return 0
        return answer
