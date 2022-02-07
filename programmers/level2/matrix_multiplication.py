# https://programmers.co.kr/learn/courses/30/lessons/12949


def solution(arr1, arr2):
    m = len(arr1)
    n = len(arr1[0])
    o = len(arr2[0])
    answer = [[0] * o for _ in range(m)]
    for i in range(m):
        for j in range(o):
            val = 0
            for k in range(n):
                val += arr1[i][k] * arr2[k][j]
            answer[i][j] = val
    return answer
