# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from collections import defaultdict


def solution(user_id, banned_id):
    distinct_banned_id = list(set(banned_id))
    _hash = defaultdict(list)
    lu = len(user_id)
    lb = len(banned_id)

    def matching(string, pattern):
        ls = len(string)
        lp = len(pattern)

        if ls != lp:
            return False

        for i in range(ls):
            if pattern[i] != "*" and string[i] != pattern[i]:
                return False
        return True

    for string in user_id:
        for pattern in distinct_banned_id:
            if matching(string, pattern):
                _hash[pattern].append(string)

    used = set()
    answer = set()

    def back_tracking(idx):
        if idx == lb:
            temp = list(used)
            temp.sort()
            temp = ",".join(temp)
            answer.add(temp)
            return

        pattern = banned_id[idx]
        for uid in _hash[pattern]:
            if uid in used:
                continue

            used.add(uid)
            back_tracking(idx + 1)
            used.remove(uid)

    back_tracking(0)
    return len(answer)
