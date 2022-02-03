# https://programmers.co.kr/learn/courses/30/lessons/12935


def solution(arr):
    arr.pop(arr.index(min(arr)))
    return [-1] if len(arr) == 0 else arr
