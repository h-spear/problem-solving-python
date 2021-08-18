# https://www.acmicpc.net/problem/1002

import math


def solution(params):
    x_1, y_1, r_1, x_2, y_2, r_2 = params
    dist = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
    answer = 0
    # 무한대 : 두 원이 같을 때
    if dist == 0 and r_1 == r_2:
        answer = -1

    # 한 점에서 만나는 경우 : 외접
    elif dist == (r_1 + r_2):
        answer = 1

    # 한 점에서 만나는 경우 : 내접
    elif dist == abs(r_1 - r_2):
        answer = 1

    # 두 점에서 만나는 경우
    elif abs(r_1 - r_2) < dist < (r_1 + r_2):
        answer = 2

    # 나머지
    else:
        answer = 0
    print(answer)


for tc in range(int(input())):
    solution(list(map(int, input().split())))
