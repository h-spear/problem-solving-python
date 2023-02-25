# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        answer = []
        maxx = max(nums)
        checker = {-1: 0}
        for i in range(0, maxx + 1):
            checker[i] = checker[i - 1] + counter[i]

        for i in range(len(nums)):
            answer.append(checker[nums[i] - 1])

        return answer
