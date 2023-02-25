# https://leetcode.com/problems/merge-strings-alternately/


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        l1 = len(word1)
        l2 = len(word2)
        i = 0
        j = 0
        while i < l1 and j < l2:
            merged += word1[i]
            merged += word2[j]
            i += 1
            j += 1

        while i < l1:
            merged += word1[i]
            i += 1

        while j < l2:
            merged += word2[j]
            j += 1

        return merged
