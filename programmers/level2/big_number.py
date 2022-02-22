# https://programmers.co.kr/learn/courses/30/lessons/42883


def solution(number, k):
    stack = []
    for n in number:
        if not stack:
            stack.append(n)
            continue

        if stack[-1] < n:
            while k and stack and stack[-1] < n:
                stack.pop()
                k -= 1
            stack.append(n)
        else:
            stack.append(n)

    while k:
        stack.pop()
        k -= 1
    return "".join(stack)
