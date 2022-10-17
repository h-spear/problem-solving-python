# https://school.programmers.co.kr/learn/courses/30/lessons/120882


def solution(score):
    temp = [x + y for x, y in score]
    temp.sort(reverse=True)
    rank = [i for i in range(1, len(score) + 1)]
    _dict = {}
    for i in range(len(score) - 1):
        if temp[i] == temp[i + 1]:
            rank[i + 1] = rank[i]

    for r, s in zip(rank, temp):
        _dict[s] = r

    return [_dict[x + y] for x, y in score]
