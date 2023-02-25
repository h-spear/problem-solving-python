# https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_result(string):
            stack = []
            for char in string:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)

        if get_result(s) != get_result(t):
            return False
        return True
