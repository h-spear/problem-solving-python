# https://school.programmers.co.kr/learn/courses/30/lessons/154539


def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            i = stack.pop()
            answer[i] = number
        stack.append(idx)

    return answer
