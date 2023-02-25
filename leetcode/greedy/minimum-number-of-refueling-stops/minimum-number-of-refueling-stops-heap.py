# https://leetcode.com/problems/minimum-number-of-refueling-stops/

import heapq


class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        stop_count = 0
        n = len(stations)
        heap = []

        i = 0
        while startFuel < target:

            while i < n and stations[i][0] <= startFuel:
                heapq.heappush(heap, -stations[i][1])
                i += 1

            if heap:
                startFuel += -heapq.heappop(heap)
                stop_count += 1
            else:
                return -1

        return stop_count
