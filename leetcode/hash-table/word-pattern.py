# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        checker1 = dict()
        checker2 = dict()
        words = s.split()
        n = len(words)

        if len(pattern) != n:
            return False

        for i in range(n):
            word = words[i]
            p = pattern[i]
            if p not in checker1:
                checker1[p] = word

            if word not in checker2:
                checker2[word] = p

            if checker1[p] != word:
                return False

            if checker2[word] != p:
                return False

        return True
