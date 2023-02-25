# https://leetcode.com/problems/reverse-string-ii/


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer = ""
        for i in range(0, len(s), 2 * k):
            answer += s[i : i + k][::-1]
            answer += s[i + k : i + 2 * k]

        return answer
