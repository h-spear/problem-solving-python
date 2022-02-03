# https://programmers.co.kr/learn/courses/30/lessons/12928

import math


def solution(n):
    if n <= 1:
        return n

    answer = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i != 0:
            continue
        # 4의 약수 1,2,4와 같이 2인 경우 중복으로 더해지지 않도록 함
        answer += i if i == n // i else (i + n // i)

    return answer


def solution2(n):
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
