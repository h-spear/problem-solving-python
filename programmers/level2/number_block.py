# https://school.programmers.co.kr/learn/courses/30/lessons/12923


def get_max_divisor(num):
    if num == 1:
        return 0

    for i in range(2, int(num ** 0.5) + 1):
        if num % i:
            continue
        if num // i >= 10000000:
            continue
        return num // i
    return 1


def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        answer.append(get_max_divisor(i))
    return answer
