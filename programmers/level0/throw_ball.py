# https://school.programmers.co.kr/learn/courses/30/lessons/120843


def solution(numbers, k):
    curr = 0
    n = len(numbers)
    for _ in range(k - 1):
        curr += 2
        curr %= n
    return numbers[curr]
