# https://leetcode.com/problems/h-index-ii/


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = citations[::-1]

        for i, citation in enumerate(citations):
            if i + 1 > citation:
                return i
        return i + 1
