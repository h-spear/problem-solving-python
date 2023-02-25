# https://leetcode.com/problems/last-stone-weight/

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 2:
            one = -heapq.heappop(heap)
            two = -heapq.heappop(heap)

            if one == two:
                continue
            else:
                new = abs(one - two)
                heapq.heappush(heap, -new)

        if heap:
            return -heapq.heappop(heap)
        return 0
