# https://leetcode.com/problems/basic-calculator-ii/


class Solution:
    def calculate(self, s: str) -> int:
        s += "!"
        stack = []
        num = ""
        multiplication = False
        division = False
        for char in s:
            if char == " ":
                continue
            elif char.isdigit():
                num += char
                continue
            else:
                stack.append(int(num))

            if multiplication:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
                multiplication = False

            if division:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 // num1)
                division = False

            num = ""
            if char == "+":
                stack.append(char)
            elif char == "-":
                stack.append(char)
            elif char == "*":
                multiplication = True
            elif char == "/":
                division = True

        for i in range(len(stack)):
            if isinstance(stack[i], int):
                continue

            if stack[i] == "-":
                stack[i + 1] *= -1
            stack[i] = 0

        return sum(stack)
