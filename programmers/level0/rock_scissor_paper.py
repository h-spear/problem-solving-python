# https://school.programmers.co.kr/learn/courses/30/lessons/120839


def solution(rsp):
    win = {"0": "5", "2": "0", "5": "2"}
    return "".join([win[n] for n in rsp])
