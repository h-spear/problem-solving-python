# https://programmers.co.kr/learn/courses/30/lessons/76501


def solution(absolutes, signs):
    answer = 0
    for i, x in enumerate(absolutes):
        answer += x if signs[i] else -x
    return answer
