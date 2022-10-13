# https://school.programmers.co.kr/learn/courses/30/lessons/120888


def solution(my_string):
    s = set(my_string)
    answer = ""
    for char in my_string:
        if char in s:
            answer += char
            s.remove(char)

    return answer
