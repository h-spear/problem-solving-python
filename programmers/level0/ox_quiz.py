# https://school.programmers.co.kr/learn/courses/30/lessons/120907


def solution(quiz):
    answer = []
    for _quiz in quiz:
        q, a = _quiz.split("=")
        if eval(q) == int(a):
            answer.append("O")
        else:
            answer.append("X")

    return answer
