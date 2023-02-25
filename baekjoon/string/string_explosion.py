# https://www.acmicpc.net/problem/9935

string = input()
bomb = list(input())

stack = []
for char in string:
    stack.append(char)
    if len(stack) < len(bomb):
        continue
    if stack[-len(bomb) :] == bomb:
        for j in range(len(bomb)):
            stack.pop()

if len(stack):
    print("".join(stack))
else:
    print("FRULA")
