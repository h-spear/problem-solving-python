# https://programmers.co.kr/learn/courses/30/lessons/42890

from collections import defaultdict
from itertools import combinations


def solution(relation):
    hash = defaultdict(set)
    row_length = len(relation[0])
    num_of_tuples = len(relation)
    for row in relation:
        for i in range(1, row_length + 1):
            for key in combinations(range(row_length), i):
                value = " ".join([str(row[i]) for i in key])
                key = " ".join(list(map(str, list(key))))
                hash[key].add(value)

    candidate_keys = set()
    answer = 0
    for key in hash:
        if len(hash[key]) != num_of_tuples:
            continue

        candidate = True
        for cand in candidate_keys:
            res = set(cand.split()) - set(key.split())
            if len(res) == 0:
                candidate = False

        if candidate == False:
            continue
        candidate_keys.add(key)
        answer += 1

    return answer
