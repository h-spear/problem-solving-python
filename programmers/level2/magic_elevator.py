# https://school.programmers.co.kr/learn/courses/30/lessons/148653


def solution(storey):
    answer = 0

    while storey:
        r = storey % 10

        if r > 5:
            answer += 10 - r
            storey += 10 - r
        elif r == 5:
            if (storey // 10) % 10 >= 5:
                storey += 10 - r
            else:
                storey -= r
            answer += r
        else:
            answer += r
            storey -= r

        storey //= 10

    return answer
