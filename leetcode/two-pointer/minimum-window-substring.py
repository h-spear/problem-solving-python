# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        counter_s = defaultdict(int)
        ls = len(s)

        def check():
            for key in counter_t:
                if counter_t[key] > counter_s[key]:
                    return False
            return True

        i = 0
        j = 1
        counter_s[s[i]] += 1
        minima = float("inf")
        answer = ""
        if check():
            minima = j - i
            answer = s[i:j]

        while j < ls:
            if check():
                length = j - i
                if length < minima:
                    answer = s[i:j]
                    minima = length

                counter_s[s[i]] -= 1
                if counter_s[s[i]] == 0:
                    del counter_s[s[i]]
                i += 1
            else:
                counter_s[s[j]] += 1
                j += 1

        while i < ls:
            if check():
                length = j - i
                if length < minima:
                    answer = s[i:j]
                    minima = length

                counter_s[s[i]] -= 1
                if counter_s[s[i]] == 0:
                    del counter_s[s[i]]
            i += 1

        return answer
