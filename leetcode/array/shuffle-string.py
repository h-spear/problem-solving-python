# https://leetcode.com/problems/shuffle-string/


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(s)
        for i, indice in enumerate(indices):
            result[indice] = s[i]
        return "".join(result)
