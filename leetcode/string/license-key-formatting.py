# https://leetcode.com/problems/license-key-formatting/


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        if not s:
            return ""

        answer = ""
        n = len(s)
        cnt = 0
        for i in range(n - 1, -1, -1):
            answer += s[i]
            cnt += 1
            if cnt == k:
                answer += "-"
                cnt = 0

        if answer[-1] == "-":
            answer = answer[:-1]

        return answer[::-1]
