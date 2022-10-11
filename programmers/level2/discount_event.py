# https://school.programmers.co.kr/learn/courses/30/lessons/131127

from collections import defaultdict


def solution(want, number, discount):
    def check():
        for i in range(lw):
            if counter[want[i]] != number[i]:
                return False
        return True

    answer = 0
    lw = len(want)
    ld = len(discount)
    counter = defaultdict(int)
    for i in range(10):
        counter[discount[i]] += 1

    i = 0
    while i < ld - 10:
        if check():
            answer += 1
        counter[discount[i]] -= 1
        counter[discount[i + 10]] += 1
        i += 1

    if check():
        answer += 1

    return answer
