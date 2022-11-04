# https://school.programmers.co.kr/learn/courses/30/lessons/133502?language=python3


def solution(ingredient):
    answer = 0
    stack = []
    ingredient.reverse()

    while ingredient:
        i = ingredient.pop()
        stack.append(i)

        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1

    return answer
