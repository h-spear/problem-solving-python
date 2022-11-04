# https://school.programmers.co.kr/learn/courses/30/lessons/134240?language=python3


def solution(food):
    answer = ""

    for i, f in enumerate(food):
        answer += str(i) * (f // 2)

    return answer + "0" + answer[::-1]
