# https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiouAEIOU"
        indexer = []
        values = []

        for i, v in enumerate(s):
            if v in vowel:
                indexer.append(i)
                values.append(v)

        s = list(s)
        values.reverse()
        for i in range(len(indexer)):
            s[indexer[i]] = values[i]

        return "".join(s)
