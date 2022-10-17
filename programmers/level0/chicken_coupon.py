# https://school.programmers.co.kr/learn/courses/30/lessons/120884


def solution(chicken):
    answer = 0
    coupon = 0
    while chicken:
        coupon += chicken
        chicken = 0

        service = coupon // 10
        coupon %= 10
        chicken += service
        answer += service

    answer += coupon // 10

    return answer
