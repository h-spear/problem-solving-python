# https://leetcode.com/problems/count-items-matching-a-rule/


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rhash = {"type": 0, "color": 1, "name": 2}
        key = rhash[ruleKey]
        answer = 0
        for item in items:
            if item[key] == ruleValue:
                answer += 1
        return answer
