# https://school.programmers.co.kr/learn/courses/30/lessons/133499

gList = ["aya", "ye", "woo", "ma"]


def judge(string):
    for pattern in gList:
        string = string.replace(pattern, "!")
        if "!!" in string:
            return False
        string = string.replace("!", "*")
    string = string.replace("*", "")
    return not string


def solution(babbling):
    answer = 0
    for string in babbling:
        if judge(string):
            answer += 1
    return answer
