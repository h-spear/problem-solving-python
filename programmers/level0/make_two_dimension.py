# https://school.programmers.co.kr/learn/courses/30/lessons/120842


def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i : i + n])
    return answer
