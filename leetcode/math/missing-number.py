# https://leetcode.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        answer = n * (n + 1) // 2
        for num in nums:
            answer -= num
        return answer
