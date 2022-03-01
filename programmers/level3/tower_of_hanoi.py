# https://programmers.co.kr/learn/courses/30/lessons/12946


def hanoi(n, _from, to, via, answer):
    if n == 1:
        answer.append([_from, to])
        return

    hanoi(n - 1, _from, via, to, answer)
    answer.append([_from, to])
    hanoi(n - 1, via, to, _from, answer)


def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer
