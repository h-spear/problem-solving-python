# https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    score = [0] * 3

    for idx, ans in enumerate(answers):
        for i in range(3):
            if ans == pattern[i][idx % len(pattern[i])]:
                score[i] += 1

    _max = max(score)

    return [i + 1 for i, x in enumerate(score) if x == _max]
