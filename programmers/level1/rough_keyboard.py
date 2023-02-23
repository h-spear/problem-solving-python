# https://school.programmers.co.kr/learn/courses/30/lessons/160586

INF = float("inf")


def solution(keymap, targets):

    counter = [INF] * 26
    for key in keymap:
        for i, _x in enumerate(key):
            x = ord(_x) - ord("A")
            counter[x] = min(counter[x], i + 1)

    answer = [0] * len(targets)

    for i, target in enumerate(targets):
        for _x in target:
            x = ord(_x) - ord("A")
            if counter[x] == INF:
                answer[i] = -1
                break
            else:
                answer[i] += counter[x]

    return answer
