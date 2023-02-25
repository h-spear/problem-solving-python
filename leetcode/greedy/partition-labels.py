# https://leetcode.com/problems/partition-labels/

from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexer = defaultdict(int)
        for i, char in enumerate(s):
            indexer[char] = i

        n = len(s)
        prev = 0
        i = 0
        j = 0
        answer = []

        while i < n:
            prev = i
            j = indexer[s[i]]
            while i < j:
                char = s[i]
                j = max(j, indexer[char])
                i += 1

            i += 1
            answer.append(i - prev)

        return answer
