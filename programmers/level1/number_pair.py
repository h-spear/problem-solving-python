# https://school.programmers.co.kr/learn/courses/30/lessons/131128

from collections import Counter


def solution(X, Y):
    counter = Counter(X) & Counter(Y)
    if not counter:
        return "-1"

    answer = ""
    for num, cnt in sorted(counter.items(), reverse=True):
        answer += num * cnt
    return "0" if answer[0] == "0" else answer
