# https://programmers.co.kr/learn/courses/30/lessons/68935


def solution(n):
    answer = 0

    li = []
    while n:
        li.append(n % 3)
        n //= 3

    for x in li:
        answer *= 3
        answer += x

    return answer
