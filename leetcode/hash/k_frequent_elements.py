# https://leetcode.com/problems/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [val for val, freq in collections.Counter(nums).most_common(k)]
