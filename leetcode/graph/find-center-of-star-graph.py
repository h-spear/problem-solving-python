# https://leetcode.com/problems/find-center-of-star-graph/

from collections import defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = defaultdict(int)
        for a, b in edges:
            counter[a] += 1
            counter[b] += 1

        return sorted(counter.items(), key=lambda x: -x[1])[0][0]
