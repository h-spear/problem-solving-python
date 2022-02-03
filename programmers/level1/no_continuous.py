# https://programmers.co.kr/learn/courses/30/lessons/12906


def solution(arr):
    answer = []
    for i, x in enumerate(arr):
        if i and x == arr[i - 1]:
            continue
        answer.append(x)
    return answer
