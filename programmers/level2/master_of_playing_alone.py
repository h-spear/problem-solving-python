# https://school.programmers.co.kr/learn/courses/30/lessons/131130


def solution(cards):
    card_counts = len(cards)
    candidates = []
    for i in range(card_counts):
        if not cards[i]:
            continue

        j = i
        cnt = 0
        while cards[j]:
            cards[j], j = 0, cards[j] - 1
            cnt += 1
        candidates.append(cnt)

    if len(candidates) == 1:
        return 0

    candidates.sort()
    return candidates[-1] * candidates[-2]
