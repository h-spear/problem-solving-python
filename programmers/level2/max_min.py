# https://programmers.co.kr/learn/courses/30/lessons/12939


def solution(s):
    nums = list(map(int, s.split()))
    return str(min(nums)) + " " + str(max(nums))
