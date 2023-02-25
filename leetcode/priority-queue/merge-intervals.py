# https://leetcode.com/problems/merge-intervals/

import heapq


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        output = []
        while intervals:
            s, e = heapq.heappop(intervals)

            while intervals and intervals[0][0] <= e:
                _, new = heapq.heappop(intervals)
                e = max(e, new)

            output.append([s, e])

        return output
