# https://school.programmers.co.kr/learn/courses/30/lessons/120853


def solution(s):
    stack = []
    lst = s.split()
    for c in lst:
        if c == "Z":
            if stack:
                stack.pop()
        else:
            stack.append(int(c))

    return sum(stack)
