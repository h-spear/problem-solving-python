# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        _dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char not in _dict:
                stack.append(char)
            else:
                pair = _dict[char]
                if not stack:
                    return False
                if stack[-1] != pair:
                    return False
                stack.pop()

        if stack:
            return False
        return True
