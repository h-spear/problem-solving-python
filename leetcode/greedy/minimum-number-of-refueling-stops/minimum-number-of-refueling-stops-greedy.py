# https://leetcode.com/problems/minimum-number-of-refueling-stops/
# greedy 풀이
# 참고: https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/?currentPage=1&orderBy=hot&query=&tag=python


class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        stop_count = 0

        stations.sort(key=lambda x: x[1], reverse=True)

        while startFuel < target:
            for i in range(len(stations)):
                if stations[i][0] <= startFuel:
                    startFuel += stations[i][1]
                    stop_count += 1
                    stations.pop(i)
                    break
            else:
                return -1

        return stop_count
