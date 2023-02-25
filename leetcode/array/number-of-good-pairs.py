# https://leetcode.com/problems/number-of-good-pairs/


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        length = len(nums)
        answer = 0
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] == nums[j]:
                    answer += 1

        return answer
