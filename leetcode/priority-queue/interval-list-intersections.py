# https://leetcode.com/problems/interval-list-intersections/

import heapq


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        answer = []
        heap = []

        for x in firstList:
            heapq.heappush(heap, x)
        for x in secondList:
            heapq.heappush(heap, x)

        while heap:
            s, e = heapq.heappop(heap)
            while heap and heap[0][0] <= e:
                ss, ee = heapq.heappop(heap)
                answer.append([ss, min(ee, e)])

                if ee > e:
                    heapq.heappush(heap, [e + 1, ee])

        return answer
