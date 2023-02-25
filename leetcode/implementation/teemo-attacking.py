# https://leetcode.com/problems/teemo-attacking/


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = 0
        last = 0
        for time in timeSeries:
            answer += time + duration - max(time, last)
            last = time + duration

        return answer
