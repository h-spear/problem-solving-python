# https://school.programmers.co.kr/learn/courses/30/lessons/147355


def solution(t, p):
    lt = len(t)
    lp = len(p)
    p = int(p)
    answer = 0

    for i in range(lt - lp + 1):
        if p >= int(t[i : i + lp]):
            answer += 1

    return answer
