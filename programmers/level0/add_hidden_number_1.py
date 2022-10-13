# https://school.programmers.co.kr/learn/courses/30/lessons/120851


def solution(my_string):
    answer = 0
    for char in my_string:
        if char.isdigit():
            answer += int(char)
    return answer
