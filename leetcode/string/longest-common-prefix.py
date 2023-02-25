# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(min(strs, key=len))
        answer = ""

        for i in range(min_len):
            find = strs[0][i]
            for s in strs:
                if s[i] != find:
                    return answer
            answer += find

        return answer
