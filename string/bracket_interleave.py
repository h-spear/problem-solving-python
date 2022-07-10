# https://www.acmicpc.net/problem/11899

s = input()
stack = []

answer = 0
for char in s:
    if char == ")":
        if not stack:
            answer += 1
        elif stack[-1] == "(":
            stack.pop()
    else:
        stack.append(char)

answer += len(stack)
print(answer)
