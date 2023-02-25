# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                diff.append(i)

        if not diff:
            return True
        elif len(diff) == 1:
            return False
        elif len(diff) > 2:
            return False

        if s1[diff[0]] != s2[diff[1]]:
            return False
        elif s1[diff[1]] != s2[diff[0]]:
            return False
        return True
