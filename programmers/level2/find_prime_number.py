# https://programmers.co.kr/learn/courses/30/parts/12230
# 코딩테스트 고득점 Kit : Bruteforce

from itertools import permutations


def is_prime_number(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    candidates = set()
    for l in range(1, len(numbers) + 1):
        for x in permutations(numbers, l):
            candidates.add(int("".join(x)))

    answer = 0
    for x in candidates:
        if x <= 1:
            continue
        if not is_prime_number(x):
            continue
        answer += 1
    return answer
