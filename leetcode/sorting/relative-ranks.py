# https://leetcode.com/problems/relative-ranks/


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        temp = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        answer = [None] * n
        medal = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        for i, (_, idx) in enumerate(temp):
            if i <= 2:
                answer[idx] = medal[i]
            else:
                answer[idx] = str(i + 1)

        return answer
