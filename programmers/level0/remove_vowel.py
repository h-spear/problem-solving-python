# https://school.programmers.co.kr/learn/courses/30/lessons/120849


def solution(my_string):
    answer = ""
    for char in my_string:
        if char not in "aeiou":
            answer += char

    return answer
