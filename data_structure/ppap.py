# https://www.acmicpc.net/problem/16120

string = input()
stack = []

for char in string:
    stack.append(char)

    if len(stack) >= 4 and "".join(stack[-4:]) == "PPAP":
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append("P")

if len(stack) == 1 and stack[0] == "P":
    print("PPAP")
else:
    print("NP")
