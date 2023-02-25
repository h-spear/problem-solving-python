# https://leetcode.com/problems/find-the-difference/

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter(s)
        answer = ""
        for char in t:
            if char in counter:
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
            else:
                answer = char

        return answer


class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        return (Counter(t) - Counter(s)).most_common(1)[0][0]
