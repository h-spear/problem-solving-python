# https://school.programmers.co.kr/learn/courses/30/lessons/120899


def solution(array):
    maxx = max(array)
    return [maxx, array.index(maxx)]
