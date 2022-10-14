# https://school.programmers.co.kr/learn/courses/15008/lessons/121685


def func(n, p):

    # climb
    route = []
    while n:
        route.append(p % 4)
        n -= 1
        p //= 4

    # calc
    curr = "Rr"
    while route:
        p = route.pop()
        if p == 0:
            curr = curr[0] * 2
        elif p == 3:
            curr = curr[1] * 2

    return curr


def solution(queries):
    answer = []
    for query in queries:
        n, p = query
        answer.append(func(n - 1, p - 1))

    return answer
