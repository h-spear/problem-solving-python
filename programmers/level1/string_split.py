# https://school.programmers.co.kr/learn/courses/30/lessons/140108


def solution(s):
    answer = 0
    x = ""
    counter = [0, 0]
    flag = False
    for char in s:
        if not flag:
            flag = True
            x = char

        if char == x:
            counter[0] += 1
        else:
            counter[1] += 1

        if counter[0] == counter[1]:
            counter = [0, 0]
            answer += 1
            flag = False

    if flag:
        answer += 1

    return answer
