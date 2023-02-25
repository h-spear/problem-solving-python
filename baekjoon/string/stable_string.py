# https://www.acmicpc.net/problem/4889

tc = 0
while 1:
    tc += 1
    s = input()

    if s[0] == "-":
        break

    stack = []
    stack2 = []
    answer = 0
    for char in s:
        if char == "{":
            stack.append(char)
        else:
            if not stack or stack[-1] == "}":
                stack.append("}")
            elif stack[-1] == "{":
                stack.pop()

    for char in stack:
        if not stack2:
            if char == "}":
                answer += 1
            stack2.append("{")
            continue

        if stack2[-1] == "{":
            if char == "{":
                answer += 1
            stack2.append("}")
        elif stack2[-1] == "}":
            if char == "}":
                answer += 1
            stack2.append("{")

    print(tc, answer, sep=". ")
