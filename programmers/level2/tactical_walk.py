# https://school.programmers.co.kr/learn/courses/30/lessons/133501


def solution(distance, scope, times):
    temp = []
    for scop, time in zip(scope, times):
        scop.sort()
        temp.append((scop, time))

    temp.sort()
    for i, x in enumerate(temp):
        scop, time = x
        scope[i] = scop
        times[i] = time

    for (left, right), (work_time, rest_time) in zip(scope, times):
        total_time = work_time + rest_time
        for i in range(left - 1, right):
            _i = i % total_time + 1
            if _i <= work_time:
                return i + 1

    return distance
