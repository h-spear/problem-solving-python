# https://school.programmers.co.kr/learn/courses/30/lessons/118666

from collections import defaultdict


def solution(survey, choices):
    answer = ""
    _hash = defaultdict(int)

    for question, choice in zip(survey, choices):
        if choice == 4:
            continue
        elif choice < 4:
            _hash[question[0]] += abs(4 - choice)
        else:
            _hash[question[1]] += abs(4 - choice)

    for x, y in ["RT", "CF", "JM", "AN"]:
        if _hash[x] >= _hash[y]:
            answer += x
        else:
            answer += y

    return answer
