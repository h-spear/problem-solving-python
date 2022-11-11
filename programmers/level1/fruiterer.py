# https://school.programmers.co.kr/learn/courses/30/lessons/135808


def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    n = (len(score) // m) * m

    for i in range(0, n, m):
        answer += score[i : i + m][-1] * m
    return answer
