# https://programmers.co.kr/learn/courses/30/lessons/12930


def solution(s):
    answer = ""
    i = 0
    s = s.lower()
    for x in s:
        if x == " ":
            answer += " "
            i = 0
            continue

        if i & 1:
            answer += x
        else:
            answer += x.upper()
        i += 1

    return answer
