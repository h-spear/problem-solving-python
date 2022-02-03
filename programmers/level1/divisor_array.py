# https://programmers.co.kr/learn/courses/30/lessons/12910


def solution(arr, divisor):
    arr = sorted([x for x in arr if x % divisor == 0])
    return arr if len(arr) else [-1]


def solution(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]
