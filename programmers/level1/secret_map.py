# https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        union = arr1[i] | arr2[i]
        tmp = []
        for _ in range(n):
            tmp.append("#" if union & 1 else " ")
            union >>= 1
        answer.append("".join(reversed(tmp)))
    return answer
