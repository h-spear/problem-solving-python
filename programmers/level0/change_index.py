# https://school.programmers.co.kr/learn/courses/30/lessons/120895


def solution(my_string, num1, num2):
    temp = list(my_string)
    temp[num1], temp[num2] = temp[num2], temp[num1]
    return "".join(temp)
