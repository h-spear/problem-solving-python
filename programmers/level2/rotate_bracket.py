# https://programmers.co.kr/learn/courses/30/lessons/76502

pair = {")": "(", "}": "{", "]": "["}


def check_pair(s):
    stack = []
    for char in s:
        if char not in pair:
            stack.append(char)
            continue
        if len(stack) == 0:
            return False
        if pair[char] != stack.pop():
            return False
    return True


def solution(s):
    if (
        (s.count("(") != s.count(")"))
        or (s.count("{") != s.count("}"))
        or (s.count("[") != s.count("]"))
    ):
        return 0
    answer = 0
    for _ in range(len(s)):
        s = s[1:] + s[0]
        if check_pair(s):
            answer += 1

    return answer
