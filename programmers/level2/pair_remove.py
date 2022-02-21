# https://programmers.co.kr/learn/courses/30/lessons/12973


def solution(s):
    stack = []
    for char in s:
        stack.append(char)

        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    return sum([len(stack) == 0])
