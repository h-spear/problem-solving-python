# https://school.programmers.co.kr/learn/courses/30/lessons/159994


def solution(cards1, cards2, goal):
    lc1, lc2 = len(cards1), len(cards2)
    idx1, idx2 = 0, 0

    for word in goal:
        if idx1 < lc1 and cards1[idx1] == word:
            idx1 += 1
        elif idx2 < lc2 and cards2[idx2] == word:
            idx2 += 1
        else:
            return "No"

    return "Yes"
