# https://programmers.co.kr/learn/courses/30/lessons/12943


def solution(num):
    cnt = 0
    while cnt <= 500 and num != 1:
        if num & 1:
            num = num * 3 + 1
        else:
            num //= 2
        cnt += 1

    return cnt if cnt < 500 else -1
