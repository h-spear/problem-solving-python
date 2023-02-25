# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def check():
            count = len(counter)
            values = counter.values()
            v = sum(values) - max(values)
            if v > k:
                return False
            else:
                return True

        counter = defaultdict(int)
        counter[s[0]] += 1
        i = 0
        j = 1
        answer = 0
        while i < j and j < len(s):
            if check():
                answer = max(answer, j - i)
                counter[s[j]] += 1
                j += 1
            else:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1

        if check():
            answer = max(answer, j - i)

        return answer
