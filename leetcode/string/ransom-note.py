# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for char in ransomNote:
            if char not in counter:
                return False

            counter[char] -= 1
            if counter[char] == 0:
                del counter[char]

        return True
