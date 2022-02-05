# https://programmers.co.kr/learn/courses/30/lessons/82612


def solution(price, money, count):
    answer = price * (sum(range(count + 1))) - money
    return max(answer, 0)
