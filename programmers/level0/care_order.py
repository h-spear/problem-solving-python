# https://school.programmers.co.kr/learn/courses/30/lessons/120835


def solution(emergency):
    answer = [0] * len(emergency)
    temp = [(e, i) for i, e in enumerate(emergency)]
    temp.sort(reverse=True)
    for i, (_, idx) in enumerate(temp):
        answer[idx] = i + 1
    return answer
