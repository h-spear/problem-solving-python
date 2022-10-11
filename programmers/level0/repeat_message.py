# https://school.programmers.co.kr/learn/courses/30/lessons/120825


def solution(my_string, n):
    answer = ""
    for char in my_string:
        answer += char * n
    return answer
