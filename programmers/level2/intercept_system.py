# https://school.programmers.co.kr/learn/courses/30/lessons/181188


def solution(targets):
    n = len(targets)
    targets.sort(key=lambda x: x[0])

    i = 0
    answer = 0
    while i < n:
        pick = targets[i]
        end = pick[1]

        while i < n - 1 and targets[i + 1][0] < end:
            end = min(end, targets[i + 1][1])
            i += 1

        answer += 1
        i += 1

    return answer
