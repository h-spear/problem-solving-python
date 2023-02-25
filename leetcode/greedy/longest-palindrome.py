# https://leetcode.com/problems/longest-palindrome/

from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(int)
        answer = 0

        for char in s:
            counter[char] += 1

        for k in counter.keys():
            v = counter[k]
            if v >= 2:
                answer += (v // 2) * 2
                counter[k] = v % 2

        for v in counter.values():
            if v:
                return answer + 1

        return answer
