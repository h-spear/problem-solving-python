# https://leetcode.com/problems/repeated-substring-pattern/


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i:
                continue
            repeat = s[:i]

            for j in range(0, n, i):
                if s[j : j + i] != repeat:
                    break
            else:
                return True

        return False
