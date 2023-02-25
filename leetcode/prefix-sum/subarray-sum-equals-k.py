# https://leetcode.com/problems/subarray-sum-equals-k/
# prefix sum + hash

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        answer = 0
        _hash = defaultdict(int)
        _hash[0] = 1

        for num in nums:
            curr += num
            extra = curr - k
            answer += _hash[extra]
            _hash[curr] += 1

        return answer
