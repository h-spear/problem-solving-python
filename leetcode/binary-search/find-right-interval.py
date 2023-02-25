# https://leetcode.com/problems/find-right-interval/

from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        answer = []
        temp = []
        for i, interval in enumerate(intervals):
            temp.append([interval, i])

        temp.sort()

        for interval in intervals:
            s, e = interval
            find = [[e - 0.5, 0], 0]
            idx = bisect_left(temp, find)
            if idx == n:
                answer.append(-1)
            else:
                answer.append(temp[idx][1])

        return answer
