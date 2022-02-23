# https://programmers.co.kr/learn/courses/30/lessons/72412

from bisect import bisect_left
from collections import defaultdict


def solution(info, query):
    answer = []
    hash = defaultdict(list)

    for data in info:
        d1, d2, d3, d4, score = data.split()
        for lang in [d1, "-"]:
            for job in [d2, "-"]:
                for career in [d3, "-"]:
                    for food in [d4, "-"]:
                        key = " ".join([lang, job, career, food])
                        hash[key].append(int(score))

    for key in hash:
        hash[key].sort()

    for data in query:
        d1, d2, d3, d4 = data.split(" and ")
        d4, score = d4.split()
        score = int(score)
        key = " ".join([d1, d2, d3, d4])
        result = len(hash[key]) - bisect_left(hash[key], score)
        answer.append(result)

    return answer
