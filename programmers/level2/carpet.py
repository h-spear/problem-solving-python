# https://programmers.co.kr/learn/courses/30/lessons/42842
# 코딩테스트 고득점 Kit : Bruteforce


def solution(brown, yellow):
    for w in range(2, brown // 2 + 1):
        for h in range(2, brown - w):
            if h > w:
                continue
            if 2 * (h + w - 2) != brown:
                continue
            if (h - 2) * (w - 2) != yellow:
                continue
            return [w, h]
    return -1
