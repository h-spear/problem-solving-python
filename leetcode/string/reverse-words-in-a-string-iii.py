# https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        frag = s.split()
        lf = len(frag)
        for i in range(lf):
            frag[i] = frag[i][::-1]

        return " ".join(frag)
