# https://school.programmers.co.kr/learn/courses/30/lessons/138475


def solution(e, starts):
    div = [0] * (e + 1)
    lst = [0] * (e + 1)

    ## 약수 개수를 한 번에 구하는 방법
    for i in range(2, e + 1):
        for j in range(1, min(e // i + 1, i)):
            div[i * j] += 2

    for i in range(1, int(e ** 0.5) + 1):
        div[i * i] += 1

    largest = div[-1]
    num = 0
    for i in range(e, 0, -1):
        if div[i] >= largest:
            largest = div[i]
            num = i
            lst[i] = i
        else:
            lst[i] = num

    return [lst[s] for s in starts]
