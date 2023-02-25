# https://leetcode.com/problems/task-scheduler/

import heapq
from collections import defaultdict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        answer = 0
        counter = defaultdict(int)
        for task in tasks:
            counter[task] += 1

        heap = []
        for key in counter:
            heapq.heappush(heap, (-counter[key], key))

        time = 0
        while heap:
            answer += time
            temp = set()
            time = n + 1
            while time and heap:
                cnt, task = heapq.heappop(heap)
                time -= 1
                answer += 1

                if cnt + 1 < 0:
                    temp.add((cnt + 1, task))

            for task in temp:
                heapq.heappush(heap, task)

        return answer
