# https://programmers.co.kr/learn/courses/30/lessons/12921


def solution(n):
    A = [1 for i in range(n + 1)]
    A[0], A[1] = 0, 0

    for i in range(2, int(n ** (1 / 2) + 1)):
        if A[i] == 1:
            # i가 소수인 경우 i를 제외한 i의 모든 배수 false
            j = 2
            while i * j <= n:
                A[i * j] = 0
                j += 1
    return sum(A)


# 다른 사람의 코드
def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)
