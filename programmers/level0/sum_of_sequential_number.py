# https://school.programmers.co.kr/learn/courses/30/lessons/120923


def solution(num, total):
    a = (total - (num - 1) * num // 2) // num
    return [a + i for i in range(num)]
