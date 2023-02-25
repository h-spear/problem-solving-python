# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def check():
            for k in counter_p:
                if counter_p[k] != counter_s[k]:
                    return False
            return True

        lp = len(p)
        ls = len(s)
        counter_p = Counter(p)
        counter_s = Counter(s[0:lp])
        i = 0
        j = lp
        answer = []

        while j < ls:
            if check():
                answer.append(i)

            counter_s[s[i]] -= 1
            if counter_s[s[i]] == 0:
                del counter_s[s[i]]

            counter_s[s[j]] += 1
            i += 1
            j += 1

        if check():
            answer.append(i)

        return answer
