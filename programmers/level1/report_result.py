# https://programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    _dict = defaultdict(set)
    counter = defaultdict(int)

    for str in report:
        reporter, bad_user = str.split()
        _dict[bad_user].add(reporter)

    for x in _dict:
        if len(_dict[x]) < k:
            continue
        for user in list(_dict[x]):
            counter[user] += 1

    for i, user in enumerate(id_list):
        answer[i] = counter[user]

    return answer
