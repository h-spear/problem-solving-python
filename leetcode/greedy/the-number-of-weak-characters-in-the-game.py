# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        answer = 0
        n = len(properties)
        properties.sort()
        dp = {}
        max_def = -1
        temp = -1

        for i in range(n - 1, -1, -1):
            atk, _def = properties[i]
            dp[atk] = max_def
            temp = max(temp, _def)
            if atk > properties[i - 1][0]:
                max_def = temp

        for atk, _def in properties:
            if dp[atk] > _def:
                answer += 1

        return answer
