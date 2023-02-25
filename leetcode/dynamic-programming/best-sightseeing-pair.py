# https://leetcode.com/problems/best-sightseeing-pair/
# https://leetcode.com/problems/best-sightseeing-pair/discuss/2263916/Very-Easy-solution-using-dynamic-programming


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = values[0] - 1
        answer = 0

        for i in range(1, len(values)):
            answer = max(answer, values[i] + dp)
            dp = max(dp - 1, values[i] - 1)
            print(answer, dp)
        return answer
