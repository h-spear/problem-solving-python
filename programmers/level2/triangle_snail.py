# https://programmers.co.kr/learn/courses/30/lessons/68645


def solution(n):
    array = [[0] * n for _ in range(n)]
    last = sum(range(n + 1))
    i, j, num = 0, 0, 1

    while num <= last:
        while i < n and array[i][j] == 0:
            array[i][j] = num
            num += 1
            i += 1
        i -= 1
        j += 1
        while j < n and array[i][j] == 0:
            array[i][j] = num
            num += 1
            j += 1
        j -= 2
        i -= 1
        while array[i][j] == 0:
            array[i][j] = num
            num += 1
            i -= 1
            j -= 1
        i += 2
        j += 1

    answer = []
    for i in range(n):
        for j in range(n):
            if array[i][j] == 0:
                continue
            answer.append(array[i][j])
    return answer
