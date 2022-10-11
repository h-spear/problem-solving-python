# https://school.programmers.co.kr/learn/courses/30/lessons/120897


def solution(n):
    answer = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer.add(i)
            answer.add(n // i)

    return sorted(list(answer))
