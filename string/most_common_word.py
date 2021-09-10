# https://leetcode.com/problems/most-common-word/


import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [
            word
            for word in re.sub("[^\w]", " ", paragraph).lower().split()
            if word not in banned
        ]
        return Counter(words).most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

answer = Solution()
print(answer.mostCommonWord(paragraph, banned))
