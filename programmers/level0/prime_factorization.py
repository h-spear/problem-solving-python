# https://school.programmers.co.kr/learn/courses/30/lessons/120852


def solution(n):
    answer = set()

    d = 2
    while n != 1:
        if n % d == 0:
            answer.add(d)
            n //= d
        else:
            d += 1

    return sorted(list(answer))
