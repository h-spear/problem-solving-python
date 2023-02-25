# https://leetcode.com/problems/max-points-on-a-line/
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1

        answer = 1
        for x1, y1 in points:
            counter = defaultdict(int)
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                slope = float("inf")

                if x2 != x1:
                    slope = (y2 - y1) / (x2 - x1)
                counter[slope] += 1

            answer = max(answer, max(counter.values()) + 1)

        return answer
