# https://school.programmers.co.kr/learn/courses/30/lessons/140107


def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k):
        top = (d * d - x * x) ** 0.5
        answer += int(top / k) + 1

    return answer
