# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lis = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if not stack:
                    lis[i] = ""
                    continue

                stack.pop()

        while stack:
            i = stack.pop()
            lis[i] = ""

        return "".join(lis)
