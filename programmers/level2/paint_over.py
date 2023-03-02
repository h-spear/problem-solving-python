# https://school.programmers.co.kr/learn/courses/30/lessons/161989


def solution(n, m, section):
    answer = 0

    last = -1
    for s in section:
        if last < s:
            last = s + m - 1
            answer += 1

    return answer
