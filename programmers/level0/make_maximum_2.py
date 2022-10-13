# https://school.programmers.co.kr/learn/courses/30/lessons/120862


def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
