# https://programmers.co.kr/learn/courses/30/lessons/17682

import re

bonus = {"S": 1, "D": 2, "T": 3}


def solution(dartResult):
    answer = 0
    dartResult = re.sub("10", "!", dartResult)
    _round = []
    option = [""] * 3

    for i, x in enumerate(dartResult):
        if x.isdigit():
            _round.append(int(x) ** bonus[dartResult[i + 1]])
            continue
        if x == "!":
            _round.append(10 ** bonus[dartResult[i + 1]])
            continue

        if x in ["*", "#"]:
            if i <= 2:
                option[0] = x
            elif i <= 5:
                option[1] = x
            else:
                option[2] = x

    for i, o in enumerate(option):
        if o == "":
            continue
        if o == "#":
            _round[i] *= -1
        if o == "*":
            _round[i] *= 2
            if i == 0:
                continue
            _round[i - 1] *= 2

    return sum(_round)
