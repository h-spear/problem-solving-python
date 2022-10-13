# https://school.programmers.co.kr/learn/courses/30/lessons/120836


def solution(n):
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n // i == i:
                answer += 1
            else:
                answer += 2
    return answer
