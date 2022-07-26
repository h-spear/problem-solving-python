# https://school.programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict


def solution(gems):
    set_gems = set(gems)
    len_set_gems = len(set_gems)
    len_gems = len(gems)
    i = 0
    j = 1
    hash = defaultdict(int)
    hash[gems[0]] += 1
    answer = None
    length = 987654321

    if len(hash) == len_set_gems:
        answer = [i + 1, j]
        length = j - i

    while i < j and j < len_gems:
        if len(hash) == len_set_gems:
            jewel = gems[i]
            hash[jewel] -= 1
            if hash[jewel] == 0:
                del hash[jewel]

            i += 1
        else:
            jewel = gems[j]
            hash[jewel] += 1
            j += 1

        if len(hash) == len_set_gems:
            if length > j - i:
                length = j - i
                answer = [i + 1, j]

    while i < j:
        jewel = gems[i]
        hash[jewel] -= 1
        if hash[jewel] == 0:
            break

        i += 1

        if len(hash) == len_set_gems:
            if length > j - i:
                length = j - i
                answer = [i + 1, j]

    return answer
