# https://leetcode.com/problems/insert-interval/

from collections import deque


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        n = int(1e1)
        q = deque(intervals)
        answer = []
        ns, ne = newInterval
        while q:
            interval = q.popleft()
            s, e = interval
            if ns <= s <= ne or ns <= e <= ne or s <= ns <= e or s <= ne <= e:
                flag = True
                ns = min(ns, s)
                ne = max(ne, e)
            else:
                answer.append(interval)

        answer.append([ns, ne])
        answer.sort()

        return answer
