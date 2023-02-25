# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

from bisect import bisect_right


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        answer = 0
        p = int(1e9) + 7

        for i in range(n):
            key = target - nums[i]
            j = bisect_right(nums, key)
            if j <= i:
                break

            answer += 1 << (j - i - 1)
            answer %= p

        return answer
