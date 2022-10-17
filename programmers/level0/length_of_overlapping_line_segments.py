# https://school.programmers.co.kr/learn/courses/30/lessons/120876


def solution(lines):
    temp = [0] * 222
    for x, y in lines:
        x, y = min(x, y), max(x, y)
        for i in range(x + 100, y + 100):
            temp[i] += 1

    answer = 0
    for x in temp:
        if x >= 2:
            answer += 1
    return answer
