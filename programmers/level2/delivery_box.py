# https://school.programmers.co.kr/learn/courses/30/lessons/131704


def solution(order):
    answer = 0
    n = len(order)
    stack = []

    o = 0
    for i in range(1, n + 1):
        if i == order[o]:
            answer += 1
            o += 1
        elif i < order[o]:
            stack.append(i)

        while stack and stack[-1] == order[o]:
            stack.pop()
            answer += 1
            o += 1

    return answer
