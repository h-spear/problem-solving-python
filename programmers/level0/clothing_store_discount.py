# https://school.programmers.co.kr/learn/courses/30/lessons/120818


def solution(price):
    discount = 0
    if price >= 500000:
        discount = 0.2
    elif price >= 300000:
        discount = 0.1
    elif price >= 100000:
        discount = 0.05
    else:
        discount = 0

    return int(price - price * discount)
