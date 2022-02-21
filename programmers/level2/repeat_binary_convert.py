# https://programmers.co.kr/learn/courses/30/lessons/70129


def solution(s):
    cnt = 0
    zero = 0
    while s != "1":
        l = len(s)
        num = s.count("1")
        s = format(num, "b")
        zero += l - num
        cnt += 1
    return [cnt, zero]
