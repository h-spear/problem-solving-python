# https://leetcode.com/problems/non-overlapping-intervals/
# greedy
# 사용하는 interval의 수를 count


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        use = 0
        n = len(intervals)
        prev = -float("inf")
        for i in range(n):
            if prev <= intervals[i][0]:
                prev = intervals[i][1]
                use += 1

        return n - use
