# https://school.programmers.co.kr/learn/courses/30/lessons/120848


def solution(n):
    fact = [0]
    f = 1
    for i in range(1, 12):
        f *= i
        fact.append(f)

    for i in range(len(fact) - 1):
        if (fact[i] < n and fact[i + 1] > n) or fact[i] == n:
            return i
