# https://school.programmers.co.kr/learn/courses/30/lessons/120845


def solution(box, n):
    a = box[0] // n
    b = box[1] // n
    c = box[2] // n
    return a * b * c
