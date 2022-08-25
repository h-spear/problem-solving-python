# https://school.programmers.co.kr/learn/courses/30/lessons/12987


def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    answer = 0
    while A and B:
        memA = A.pop()
        memB = B.pop()
        while B and memB <= memA:
            memB = B.pop()
        if memB > memA:
            answer += 1

    return answer
