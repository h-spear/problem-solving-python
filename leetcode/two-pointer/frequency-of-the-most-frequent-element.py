# https://leetcode.com/problems/frequency-of-the-most-frequent-element/


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        j = 1
        curr = nums[0]
        answer = 0
        while i < j and j < n:
            if (j - i) * nums[j - 1] - curr <= k:
                answer = max(answer, j - i)
                curr += nums[j]
                j += 1
            else:
                curr -= nums[i]
                i += 1

        while i < n:
            if (j - i) * nums[j - 1] - curr <= k:
                answer = max(answer, j - i)
            curr -= nums[i]
            i += 1

        return answer
