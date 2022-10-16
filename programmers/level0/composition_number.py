# https://school.programmers.co.kr/learn/courses/30/lessons/120846


def get_factor_count(n):
    if n == 1:
        return 1

    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += 1
    return answer


def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if get_factor_count(i) >= 3:
            answer += 1
    return answer
