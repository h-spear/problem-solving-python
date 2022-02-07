# https://programmers.co.kr/learn/courses/30/lessons/12909


def solution(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
            continue
        if len(stack) == 0:
            return False
        stack.pop()
    return len(stack) == 0
