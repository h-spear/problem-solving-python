# https://school.programmers.co.kr/learn/courses/30/lessons/120834


def solution(age):
    alpha = [a for a in "abcdefghij"]
    answer = ""
    for num in str(age):
        answer += alpha[int(num)]
    return answer
