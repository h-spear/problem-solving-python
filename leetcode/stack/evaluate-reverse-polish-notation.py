# https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                op = token
                num1 = stack.pop()
                num2 = stack.pop()
                result = eval("(%s) %s (%s)" % (num2, op, num1))
                result = int(result)
                stack.append(str(result))
            else:
                stack.append(token)

        return stack.pop()
