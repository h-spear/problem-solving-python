# https://leetcode.com/problems/maximum-performance-of-a-team/

import heapq


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        arr = [(e, s) for e, s in zip(efficiency, speed)]
        arr.sort(reverse=True)
        heap = []
        adder = 0
        answer = 0
        for e, s in arr:
            heapq.heappush(heap, s)
            adder += s
            answer = max(answer, adder * e)
            if len(heap) == k:
                removed = heapq.heappop(heap)
                adder -= removed

        return answer % (int(1e9) + 7)
