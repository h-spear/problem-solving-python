# https://www.acmicpc.net/problem/2504

s = input()
ls = len(s)
stack = []
pair = {")": ("(", 2), "]": ("[", 3)}
flag = True
if ls <= 1:
    flag = False

if flag:
    for char in s:
        if char in "([":
            stack.append(char)
        else:
            if not stack:
                flag = False
                break

            p, score = pair[char]
            temp = 1
            _p = ""
            if stack[-1].isdigit():
                temp = int(stack.pop())

            if not stack:
                flag = False
                break

            _p = stack.pop()
            if _p != p:
                flag = False
                break

            stack.append(str(score * temp))

            while len(stack) >= 2 and stack[-1].isdigit() and stack[-2].isdigit():
                a = int(stack.pop())
                b = int(stack.pop())
                c = str(a + b)
                stack.append(c)

if len(stack) != 1 or not stack[0].isdigit():
    flag = False

if flag:
    print(stack.pop())
else:
    print(0)
