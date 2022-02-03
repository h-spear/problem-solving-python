# https://programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos, win_nums):
    unknown = lottos.count(0)
    correct = 0
    for x in lottos:
        if x in win_nums:
            correct += 1

    _max = 7 - (unknown + correct) if (unknown + correct) >= 2 else 6
    _min = (7 - correct) if correct >= 2 else 6
    return [_max, _min]
