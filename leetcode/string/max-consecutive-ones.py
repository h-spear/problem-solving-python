# https://leetcode.com/problems/max-consecutive-ones/

import re


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = "".join(map(str, nums))
        answer = 0
        for fragment in re.findall("1+", s):
            answer = max(answer, len(fragment))
        return answer
