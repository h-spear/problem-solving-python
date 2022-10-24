# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import defaultdict


def solution(topping):
    def add_for_A(i):
        t = topping[i]
        hash_A[t] += 1

    def pop_for_B(i):
        t = topping[i]
        hash_B[t] -= 1
        if hash_B[t] == 0:
            del hash_B[t]

    def check():
        if len(hash_A) == len(hash_B):
            return 1
        return 0

    def atomic(i):
        add_for_A(i)
        pop_for_B(i)
        return check()

    answer = 0
    n = len(topping)
    hash_A = defaultdict(int)
    hash_B = defaultdict(int)
    for x in topping:
        hash_B[x] += 1

    for i in range(n):
        answer += atomic(i)
    return answer
