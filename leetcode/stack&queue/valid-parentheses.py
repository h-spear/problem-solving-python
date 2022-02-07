# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            if char in [")", "]", "}"]:
                if len(stack) == 0:
                    return False
                if stack.pop() != pair[char]:
                    return False
        if len(stack):
            return False
        return True
