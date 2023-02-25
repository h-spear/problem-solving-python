# https://leetcode.com/problems/h-index/


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for i, citation in enumerate(citations):
            if i + 1 > citation:
                return i
        return i + 1
