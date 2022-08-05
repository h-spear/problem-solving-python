# https://school.programmers.co.kr/learn/courses/30/lessons/12938


def solution(n, s):
    q = s // n
    r = s % n
    if q <= 0:
        return [-1]

    answer = []
    for _ in range(n - r):
        answer.append(q)
    for _ in range(r):
        answer.append(q + 1)

    return answer
