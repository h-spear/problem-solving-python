# https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _hash = dict()
        for num in nums:
            if num not in _hash:
                _hash[num] = 1
                continue
            return True
        return False
