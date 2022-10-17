# https://school.programmers.co.kr/learn/courses/30/lessons/120868


def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def solution(sides):
    a, b = sides
    answer = 0
    for x in range(1, 2000):
        answer += is_triangle(a, b, x)
    return answer
