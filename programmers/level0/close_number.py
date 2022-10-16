# https://school.programmers.co.kr/learn/courses/30/lessons/120890


def solution(array, n):
    m = 123456789
    answer = 0
    array.sort()
    for num in array:
        if abs(num - n) < m:
            m = abs(num - n)
            answer = num
    return answer
