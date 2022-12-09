# https://school.programmers.co.kr/learn/courses/30/lessons/142086


def solution(s):
    checker = {}
    answer = []

    for i, char in enumerate(s):
        if char not in checker:
            answer.append(-1)
            checker[char] = i
        else:
            answer.append(i - checker[char])
            checker[char] = i

    return answer
