# https://programmers.co.kr/learn/courses/30/lessons/12947


def solution(x):
    return x % sum(list(map(int, list(str(x))))) == 0
