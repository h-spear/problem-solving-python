# https://programmers.co.kr/learn/courses/30/lessons/77884

import math


def check_factor(num):
    cnt = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            cnt += 2
        if num / i == i:
            cnt -= 1
    return -1 if cnt & 1 else 1


def solution(left, right):
    answer = 0
    for x in range(left, right + 1):
        answer += x * check_factor(x)
    return answer


####################################
def solution2(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        sqrt = math.sqrt(i)
        # 약수의 개수가 홀수
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i

    return answer
