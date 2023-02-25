# https://leetcode.com/problems/top-k-frequent-words/

from collections import defaultdict


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = defaultdict(int)
        while words:
            word = words.pop()
            counter[word] += 1

        sa = sorted(
            [(cnt, word) for word, cnt in counter.items()], key=lambda x: (-x[0], x[1])
        )

        return [word for cnt, word in sa][:k]
