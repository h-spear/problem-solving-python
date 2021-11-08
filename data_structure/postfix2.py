# https://www.acmicpc.net/problem/1935

operator = ["+", "-", "*", "/"]
operand = [0] * 26
stack = []

n = int(input())
exp = input()

for i in range(n):
    operand[i] = int(input())

for now in exp:
    if now in operator:
        y = stack.pop()
        x = stack.pop()
        if now == "+":
            stack.append(x + y)
        elif now == "-":
            stack.append(x - y)
        elif now == "*":
            stack.append(x * y)
        elif now == "/":
            stack.append(x / y)
        else:
            exit()
    else:
        stack.append(operand[ord(now) - ord("A")])

print("{:.2f}".format(stack.pop()))
