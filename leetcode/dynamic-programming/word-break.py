# https://leetcode.com/problems/word-break/


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        checker = [False] * (n + 1)
        checker[n] = True
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                length = len(word)
                if s[i : i + length] == word:
                    checker[i] = checker[i + length]

                if checker[i]:
                    break

        return checker[0]
