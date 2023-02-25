# https://leetcode.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                temp = ""
                while stack:
                    c = stack.pop()
                    if c == "[":
                        break
                    temp += c

                num = ""
                while stack:
                    if not stack[-1].isdigit():
                        break
                    num += stack.pop()

                temp = temp[::-1]
                num = int(num[::-1])

                for _ in range(num):
                    for t in temp:
                        stack.append(t)
            else:
                stack.append(char)

        return "".join(stack)
