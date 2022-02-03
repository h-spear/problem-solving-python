# https://programmers.co.kr/learn/courses/30/lessons/12982


def solution(d, budget):
    answer = 0
    d.sort()
    for x in d:
        if x > budget:
            break
        answer += 1
        budget -= x
    return answer
