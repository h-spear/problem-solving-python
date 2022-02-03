# https://programmers.co.kr/learn/courses/30/lessons/12925


def solution(s):
    answer = 0
    tmp = ""
    for x in s:
        if x in ["-", "+"]:
            if tmp == "":
                tmp += x
                continue
            answer += int(tmp)
        tmp += x
    answer += int(tmp)
    return answer


# 부호가 포함되어도 int로 알아서 인식함
def solution(s):
    return int(s)
