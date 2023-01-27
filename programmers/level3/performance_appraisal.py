# https://school.programmers.co.kr/learn/courses/30/lessons/152995


def solution(scores):
    n = len(scores)

    for i in range(n):
        if scores[i][0] > scores[0][0] and scores[i][1] > scores[0][1]:
            return -1

    sum_wanho = sum(scores[0])
    scores.sort(key=lambda x: (x[0], -x[1]))
    maxx = scores[-1][1]
    answer = 1

    for i in range(n - 1, -1, -1):
        a, b = scores[i]
        maxx = max(maxx, scores[i][1])
        if b < maxx and a < scores[-1][0]:
            continue

        if a + b > sum_wanho:
            answer += 1

    return answer
