# https://leetcode.com/problems/permutation-in-string/

from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def counter_check():
            for k in _hash:
                if _hash[k] != counter[k]:
                    return False
            return True

        counter = Counter(s1)
        _hash = defaultdict(int)
        ls1 = len(s1)
        ls2 = len(s2)

        if ls1 > ls2:
            return False

        for i in range(ls1):
            _hash[s2[i]] += 1

        if counter_check():
            return True

        i = 0
        j = ls1
        while j < ls2:
            _hash[s2[j]] += 1
            _hash[s2[i]] -= 1
            if _hash[s2[i]] == 0:
                del _hash[s2[i]]
            i += 1
            j += 1

            if counter_check():
                return True

        return False
