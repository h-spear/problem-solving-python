# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s = dict()
        hash_t = dict()
        idxs_s = []
        idxs_t = []
        for i, (char1, char2) in enumerate(zip(s, t)):
            if char1 not in hash_s:
                hash_s[char1] = i
                idxs_s.append(i)
            else:
                idxs_s.append(hash_s[char1])

            if char2 not in hash_t:
                hash_t[char2] = i
                idxs_t.append(i)
            else:
                idxs_t.append(hash_t[char2])

        for i, j in zip(idxs_s, idxs_t):
            if i != j:
                return False
        return True
