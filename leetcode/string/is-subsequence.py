# https://leetcode.com/problems/is-subsequence/submissions/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        ls = len(s)
        while i < ls:
            char = s[i]
            if char in t:
                t = t[t.index(char) + 1 :]
                i += 1
            else:
                return False

        return True


# 느림
import re


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pattern = ".*"
        pattern += ".*".join(s)
        pattern += ".*"
        if re.match(pattern, t):
            return True
        return False
