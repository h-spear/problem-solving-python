# https://leetcode.com/problems/majority-element/

from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        b = n // 2
        counter = Counter(nums)
        for k, v in counter.items():
            if v > b:
                return k
